#!/bin/bash
# SpecKit Salesforce Installer
# Installs SpecKit for any Salesforce development project

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

clear
echo ""
echo -e "${CYAN}╔════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║        ${BOLD}SpecKit - Salesforce Development Accelerator${NC}${CYAN}           ║${NC}"
echo -e "${CYAN}║                    Salesforce Edition v1.0                     ║${NC}"
echo -e "${CYAN}╠════════════════════════════════════════════════════════════════╣${NC}"
echo -e "${CYAN}║   • Intent-driven specifications                               ║${NC}"
echo -e "${CYAN}║   • Progress dashboard with GitHub Pages                       ║${NC}"
echo -e "${CYAN}║   • Jira integration & status sync                             ║${NC}"
echo -e "${CYAN}║   • Multi-contributor token tracking                           ║${NC}"
echo -e "${CYAN}║   • Memory files (taxonomy, domain, regulatory)                ║${NC}"
echo -e "${CYAN}║   • Salesforce Constitution governance                         ║${NC}"
echo -e "${CYAN}╚════════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Target directory
if [ -z "$1" ]; then
    echo -e "${BLUE}Where would you like to install SpecKit?${NC}"
    read -p "Target directory (. for current): " TARGET_DIR
    TARGET_DIR="${TARGET_DIR:-.}"
else
    TARGET_DIR="$1"
fi

[ "$TARGET_DIR" = "." ] && TARGET_DIR="$(pwd)" || { mkdir -p "$TARGET_DIR" 2>/dev/null; TARGET_DIR="$(cd "$TARGET_DIR" && pwd)"; }

echo ""
echo -e "${BLUE}📁 Install location: ${BOLD}$TARGET_DIR${NC}"
echo ""
read -p "Proceed? (Y/n): " CONFIRM
[[ ! "${CONFIRM:-Y}" =~ ^[Yy]$ ]] && echo "Cancelled." && exit 0

echo ""
echo -e "${BLUE}📦 Installing components...${NC}"
cp -r "$SCRIPT_DIR/.specify" "$TARGET_DIR/" && echo -e "  ${GREEN}✓${NC} SpecKit core"
mkdir -p "$TARGET_DIR/.cursor" && cp -r "$SCRIPT_DIR/.cursor/skills" "$TARGET_DIR/.cursor/" && echo -e "  ${GREEN}✓${NC} Agent skills (12 commands)"
cp -r "$SCRIPT_DIR/docs" "$TARGET_DIR/" && echo -e "  ${GREEN}✓${NC} Progress dashboard"
mkdir -p "$TARGET_DIR/specs" && echo -e "  ${GREEN}✓${NC} Specs directory"
find "$TARGET_DIR/.specify/scripts" -name "*.sh" -exec chmod +x {} \; 2>/dev/null

echo ""
echo -e "${CYAN}════════════════════════════════════════════════════════════════${NC}"
echo -e "${BOLD}                    PROJECT CONFIGURATION${NC}"
echo -e "${CYAN}════════════════════════════════════════════════════════════════${NC}"
echo ""

# Project Name
while [ -z "$PROJECT_NAME" ]; do
    read -p "$(echo -e ${BOLD}Project Name${NC} [required]: )" PROJECT_NAME
    [ -z "$PROJECT_NAME" ] && echo -e "${RED}  Project name is required${NC}"
done

# Salesforce Org
echo ""
read -p "$(echo -e ${BOLD}Salesforce Org Alias${NC}: )" SF_ORG
SF_ORG="${SF_ORG:-default}"

# GitHub
echo ""
echo -e "${BLUE}─── GitHub Configuration ───${NC}"
echo -e "${YELLOW}Full URL to your repository (for dashboard links)${NC}"
echo -e "${YELLOW}Example: https://github.com/myorg/my-project${NC}"
read -p "GitHub URL: " GITHUB_REPO

# Jira
echo ""
echo -e "${BLUE}─── Jira Configuration ───${NC}"
echo -e "${YELLOW}For story status sync${NC}"
read -p "Jira Project Key (e.g., MYPROJ): " JIRA_KEY
if [ -n "$JIRA_KEY" ]; then
    echo -e "${YELLOW}Example: https://company.atlassian.net/jira/software/projects/MYPROJ/boards/1${NC}"
    read -p "Jira Board URL: " JIRA_URL
fi

# Contributor
echo ""
echo -e "${BLUE}─── Your Information ───${NC}"
read -p "Your Name: " CONTRIBUTOR_NAME
CONTRIBUTOR_NAME="${CONTRIBUTOR_NAME:-Developer}"
read -p "Your Role: " CONTRIBUTOR_ROLE
CONTRIBUTOR_ROLE="${CONTRIBUTOR_ROLE:-Developer}"

CONTRIBUTOR_ID=$(echo "$CONTRIBUTOR_NAME" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | cut -c1-20)
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

echo ""
echo -e "${BLUE}⚙️  Saving configuration...${NC}"

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
    "note": "Token estimates based on conversation session length.",
    "total_estimated_tokens": 0,
    "by_contributor": [],
    "by_epic": []
  },
  "deployment_status": {
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
echo -e "  ${GREEN}✓${NC} Configuration saved"

# Git
if [ ! -d "$TARGET_DIR/.git" ]; then
    read -p "Initialize git repository? (Y/n): " INIT_GIT
    [[ "${INIT_GIT:-Y}" =~ ^[Yy]$ ]] && cd "$TARGET_DIR" && git init -q && echo -e "  ${GREEN}✓${NC} Git initialized"
fi

echo ""
echo -e "${GREEN}╔════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║              ✅ Installation Complete!                         ║${NC}"
echo -e "${GREEN}╚════════════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "  ${CYAN}Project:${NC}  $PROJECT_NAME"
echo -e "  ${CYAN}Location:${NC} $TARGET_DIR"
echo -e "  ${CYAN}SF Org:${NC}   $SF_ORG"
[ -n "$GITHUB_REPO" ] && echo -e "  ${CYAN}GitHub:${NC}   $GITHUB_REPO"
[ -n "$JIRA_KEY" ] && echo -e "  ${CYAN}Jira:${NC}     $JIRA_KEY"
echo ""
echo -e "${CYAN}═══════════════════ NEXT STEPS ═══════════════════${NC}"
echo ""
echo -e "  1. Open in Cursor: ${YELLOW}cursor $TARGET_DIR${NC}"
echo -e "  2. First spec:     ${YELLOW}/speckit-specify -EPIC \"Name\" Objective: ...${NC}"
echo -e "  3. Generate plan:  ${YELLOW}/speckit-plan${NC}"
echo -e "  4. Create tasks:   ${YELLOW}/speckit-tasks${NC}"
echo -e "  5. Dashboard:      ${YELLOW}/speckit-dashboard${NC}"
[ -n "$GITHUB_REPO" ] && echo -e "  6. GitHub Pages:   Settings → Pages → /docs"
echo ""
