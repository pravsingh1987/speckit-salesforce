#!/usr/bin/env python3
"""SpecKit Salesforce CLI - Install and manage SpecKit for Salesforce projects."""

import os
import sys
import json
import shutil
import subprocess
from pathlib import Path
from datetime import datetime
from importlib import resources

import click
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich import print as rprint

console = Console()

PACKAGE_NAME = "speckit_salesforce"
VERSION = "1.0.0"

# Asset URLs for downloading
GITHUB_RAW_URL = "https://raw.githubusercontent.com/pravsingh1987/speckit-salesforce/main"
SOMA_RAW_URL = "https://git.soma.salesforce.com/raw/praveensingh/speckit-salesforce/main"


def get_assets_path() -> Path:
    """Get the path to bundled assets."""
    try:
        with resources.files(PACKAGE_NAME).joinpath("assets") as assets_path:
            return Path(assets_path)
    except (TypeError, FileNotFoundError):
        # Fallback for development
        return Path(__file__).parent / "assets"


def print_banner():
    """Print the SpecKit banner."""
    banner = """
╔════════════════════════════════════════════════════════════════╗
║        [bold cyan]SpecKit - Salesforce Development Accelerator[/bold cyan]           ║
║                    Salesforce Edition v1.0                     ║
╠════════════════════════════════════════════════════════════════╣
║   • Intent-driven specifications                               ║
║   • Progress dashboard with GitHub Pages                       ║
║   • Jira integration & status sync                             ║
║   • Multi-contributor token tracking                           ║
║   • Memory files (taxonomy, domain, regulatory)                ║
║   • Salesforce Constitution governance                         ║
╚════════════════════════════════════════════════════════════════╝
"""
    rprint(banner)


def download_assets(target_dir: Path, use_soma: bool = True) -> bool:
    """Download SpecKit assets from GitHub."""
    base_url = SOMA_RAW_URL if use_soma else GITHUB_RAW_URL
    
    # For now, we'll use git clone in a temp directory
    # In production, you'd bundle assets or use releases
    console.print("[yellow]Downloading SpecKit assets...[/yellow]")
    
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_url = (
            "https://git.soma.salesforce.com/praveensingh/speckit-salesforce.git"
            if use_soma else
            "https://github.com/pravsingh1987/speckit-salesforce.git"
        )
        
        try:
            result = subprocess.run(
                ["git", "clone", "--depth", "1", repo_url, tmpdir],
                capture_output=True,
                text=True,
                timeout=60
            )
            
            if result.returncode != 0:
                console.print(f"[red]Failed to download assets: {result.stderr}[/red]")
                return False
            
            # Copy assets to target
            tmp_path = Path(tmpdir)
            
            # Copy .specify
            if (tmp_path / ".specify").exists():
                shutil.copytree(tmp_path / ".specify", target_dir / ".specify", dirs_exist_ok=True)
            
            # Copy .cursor/skills
            if (tmp_path / ".cursor" / "skills").exists():
                (target_dir / ".cursor").mkdir(exist_ok=True)
                shutil.copytree(tmp_path / ".cursor" / "skills", target_dir / ".cursor" / "skills", dirs_exist_ok=True)
            
            # Copy docs
            if (tmp_path / "docs").exists():
                shutil.copytree(tmp_path / "docs", target_dir / "docs", dirs_exist_ok=True)
            
            # Create specs directory
            (target_dir / "specs").mkdir(exist_ok=True)
            
            return True
            
        except subprocess.TimeoutExpired:
            console.print("[red]Download timed out. Please check your network connection.[/red]")
            return False
        except Exception as e:
            console.print(f"[red]Error downloading assets: {e}[/red]")
            return False


def configure_project(target_dir: Path) -> dict:
    """Interactive project configuration."""
    config = {}
    
    # Step 1: Constitution
    rprint("\n[magenta]╔════════════════════════════════════════════════════════════════╗[/magenta]")
    rprint("[magenta]║  [bold]STEP 1 of 5: SALESFORCE CONSTITUTION[/bold]                         ║[/magenta]")
    rprint("[magenta]╚════════════════════════════════════════════════════════════════╝[/magenta]\n")
    
    rprint("[yellow]The Constitution defines your project's governance rules:[/yellow]")
    rprint("  • Architectural principles (platform-first, no technical debt)")
    rprint("  • Security standards (user mode, CRUD/FLS, sharing)")
    rprint("  • Governor limits & bulkification rules")
    rprint("  • Code quality standards (trigger patterns, testing)")
    
    config["open_constitution"] = Confirm.ask("\nWould you like to customize the constitution after installation?", default=False)
    
    # Step 2: Memory Files
    rprint("\n[magenta]╔════════════════════════════════════════════════════════════════╗[/magenta]")
    rprint("[magenta]║  [bold]STEP 2 of 5: MEMORY FILES (Project Context)[/bold]                  ║[/magenta]")
    rprint("[magenta]╚════════════════════════════════════════════════════════════════╝[/magenta]\n")
    
    rprint("[yellow]Memory files are automatically consulted by all SpecKit commands.[/yellow]\n")
    
    config["project_name"] = Prompt.ask("[bold]Project Name[/bold]", default="My Salesforce Project")
    config["sf_org"] = Prompt.ask("[bold]Salesforce Org Alias[/bold]", default="default")
    
    rprint("\n[blue]What industry/domain is this project for?[/blue]")
    rprint("  [bold]1[/bold]) Healthcare / Life Sciences / Pharma")
    rprint("  [bold]2[/bold]) Financial Services / Banking / Insurance")
    rprint("  [bold]3[/bold]) Manufacturing / Supply Chain")
    rprint("  [bold]4[/bold]) Retail / E-commerce")
    rprint("  [bold]5[/bold]) Technology / SaaS")
    rprint("  [bold]6[/bold]) Other / General")
    
    industry_choice = Prompt.ask("\nChoice", default="6")
    industries = {
        "1": "Healthcare / Life Sciences",
        "2": "Financial Services",
        "3": "Manufacturing",
        "4": "Retail",
        "5": "Technology",
        "6": "General"
    }
    config["industry"] = industries.get(industry_choice, "General")
    
    # Step 3: Templates
    rprint("\n[magenta]╔════════════════════════════════════════════════════════════════╗[/magenta]")
    rprint("[magenta]║  [bold]STEP 3 of 5: TEMPLATES & EXTENSIONS[/bold]                          ║[/magenta]")
    rprint("[magenta]╚════════════════════════════════════════════════════════════════╝[/magenta]\n")
    
    rprint("[yellow]Templates define the output format for SpecKit commands.[/yellow]")
    rprint("  [bold]spec-template.md[/bold]    - Feature specifications with user stories")
    rprint("  [bold]plan-template.md[/bold]    - Implementation plans with constitution check")
    rprint("  [bold]tasks-template.md[/bold]   - Task breakdown organized by user story")
    rprint("\n[green]✓[/green] Templates are pre-configured and ready to use.")
    
    # Step 4: Integrations
    rprint("\n[magenta]╔════════════════════════════════════════════════════════════════╗[/magenta]")
    rprint("[magenta]║  [bold]STEP 4 of 5: INTEGRATIONS[/bold]                                     ║[/magenta]")
    rprint("[magenta]╚════════════════════════════════════════════════════════════════╝[/magenta]\n")
    
    rprint("[blue]─── GitHub Configuration ───[/blue]")
    rprint("[dim]For dashboard links and GitHub Pages hosting[/dim]")
    config["github_repo"] = Prompt.ask("GitHub Repository URL (press Enter to skip)", default="")
    
    rprint("\n[blue]─── Jira Configuration ───[/blue]")
    rprint("[dim]For story status sync and progress tracking[/dim]")
    config["jira_key"] = Prompt.ask("Jira Project Key (e.g., MYPROJ, press Enter to skip)", default="")
    
    if config["jira_key"]:
        config["jira_url"] = Prompt.ask("Jira Board URL", default="")
    else:
        config["jira_url"] = ""
    
    # Step 5: Contributor
    rprint("\n[magenta]╔════════════════════════════════════════════════════════════════╗[/magenta]")
    rprint("[magenta]║  [bold]STEP 5 of 5: CONTRIBUTOR SETUP[/bold]                                ║[/magenta]")
    rprint("[magenta]╚════════════════════════════════════════════════════════════════╝[/magenta]\n")
    
    rprint("[yellow]Your information for token tracking and dashboard[/yellow]\n")
    config["contributor_name"] = Prompt.ask("Your Name", default="Developer")
    config["contributor_role"] = Prompt.ask("Your Role", default="Developer")
    
    return config


def save_configuration(target_dir: Path, config: dict):
    """Save project configuration to files."""
    # Generate contributor ID
    contributor_id = config["contributor_name"].lower().replace(" ", "-")[:20]
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    
    # Create progress-tracker.json
    tracker_data = {
        "project": {
            "name": config["project_name"],
            "industry": config["industry"],
            "jira_project": config.get("jira_key", ""),
            "jira_url": config.get("jira_url", ""),
            "github_repo": config.get("github_repo", ""),
            "salesforce_org": config["sf_org"],
            "last_updated": timestamp
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
                "id": contributor_id,
                "name": config["contributor_name"],
                "role": config["contributor_role"],
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
            "last_deployment": None,
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
    
    docs_dir = target_dir / "docs"
    docs_dir.mkdir(exist_ok=True)
    
    with open(docs_dir / "progress-tracker.json", "w") as f:
        json.dump(tracker_data, f, indent=2)
    
    # Update constitution with project name
    constitution_path = target_dir / ".specify" / "memory" / "constitution.md"
    if constitution_path.exists():
        content = constitution_path.read_text()
        content = content.replace("[YOUR-PROJECT]", config["project_name"])
        content = content.replace("[Your Organization]", config["project_name"])
        content = content.replace("[YOUR-ORG-ALIAS]", config["sf_org"])
        constitution_path.write_text(content)
    
    # Update project-details.md
    project_details_path = target_dir / ".specify" / "memory" / "project-details.md"
    if project_details_path.exists():
        content = project_details_path.read_text()
        content = content.replace("[Your Project Name]", config["project_name"])
        content = content.replace("[e.g., my-dev-org]", config["sf_org"])
        project_details_path.write_text(content)
    
    # Update domain.md with industry
    domain_path = target_dir / ".specify" / "memory" / "domain.md"
    if domain_path.exists():
        content = domain_path.read_text()
        content = content.replace("[e.g., Healthcare, Financial Services, Manufacturing, Retail]", config["industry"])
        domain_path.write_text(content)


@click.group()
@click.version_option(version=VERSION, prog_name="speckit-salesforce")
def main():
    """SpecKit Salesforce - Development Accelerator for Salesforce Projects.
    
    Install and manage SpecKit for your Salesforce development projects.
    """
    pass


@main.command()
@click.argument("target_dir", type=click.Path(), default=".")
@click.option("--use-github", is_flag=True, help="Use public GitHub instead of git.soma")
@click.option("--skip-config", is_flag=True, help="Skip interactive configuration")
def init(target_dir: str, use_github: bool, skip_config: bool):
    """Initialize a new SpecKit project.
    
    TARGET_DIR is the directory to install SpecKit into (defaults to current directory).
    
    Examples:
    
        speckit init                    # Install in current directory
        
        speckit init ./my-project       # Install in ./my-project
        
        speckit init --use-github .     # Use public GitHub for download
    """
    print_banner()
    
    target_path = Path(target_dir).resolve()
    
    if not target_path.exists():
        target_path.mkdir(parents=True)
        console.print(f"[green]✓[/green] Created directory: {target_path}")
    
    console.print(f"\n[blue]📁 Install location:[/blue] [bold]{target_path}[/bold]\n")
    
    if not Confirm.ask("Proceed with installation?", default=True):
        console.print("Cancelled.")
        return
    
    # Download assets
    console.print("\n[blue]📦 Installing SpecKit components...[/blue]")
    
    if not download_assets(target_path, use_soma=not use_github):
        console.print("[red]Installation failed. Please try again or use manual installation.[/red]")
        sys.exit(1)
    
    console.print("[green]✓[/green] SpecKit core installed")
    console.print("[green]✓[/green] Agent skills (12 commands)")
    console.print("[green]✓[/green] Progress dashboard")
    console.print("[green]✓[/green] Specs directory")
    
    # Configure project
    if not skip_config:
        config = configure_project(target_path)
        
        console.print("\n[blue]⚙️  Saving configuration...[/blue]")
        save_configuration(target_path, config)
        console.print("[green]✓[/green] Configuration saved")
        
        # Initialize git if requested
        if not (target_path / ".git").exists():
            if Confirm.ask("\nInitialize git repository?", default=True):
                subprocess.run(["git", "init", "-q"], cwd=target_path)
                console.print("[green]✓[/green] Git initialized")
    
    # Print completion message
    rprint("\n[green]╔════════════════════════════════════════════════════════════════╗[/green]")
    rprint("[green]║              ✅ Installation Complete!                         ║[/green]")
    rprint("[green]╚════════════════════════════════════════════════════════════════╝[/green]\n")
    
    rprint("[cyan]Next Steps:[/cyan]")
    rprint(f"  1. Open in Cursor: [yellow]cursor {target_path}[/yellow]")
    rprint("  2. Review constitution: [yellow]/speckit-constitution[/yellow]")
    rprint("  3. Create first spec: [yellow]/speckit-specify -EPIC \"Feature Name\"[/yellow]")
    rprint("  4. Generate plan: [yellow]/speckit-plan[/yellow]")
    rprint("")


@main.command()
@click.argument("target_dir", type=click.Path(exists=True), default=".")
@click.option("--use-github", is_flag=True, help="Use public GitHub instead of git.soma")
@click.option("--all", "update_all", is_flag=True, help="Update all components")
@click.option("--skills", is_flag=True, help="Update agent skills only")
@click.option("--templates", is_flag=True, help="Update templates only")
@click.option("--dashboard", is_flag=True, help="Update dashboard only")
def update(target_dir: str, use_github: bool, update_all: bool, skills: bool, templates: bool, dashboard: bool):
    """Update an existing SpecKit project with latest features.
    
    TARGET_DIR is the SpecKit project to update (defaults to current directory).
    
    Examples:
    
        speckit update                  # Update current directory
        
        speckit update --all            # Update all components
        
        speckit update --skills         # Update skills only
    """
    target_path = Path(target_dir).resolve()
    
    # Verify it's a SpecKit project
    if not (target_path / ".specify").exists() and not (target_path / ".cursor" / "skills").exists():
        console.print("[red]Error: This doesn't appear to be a SpecKit project[/red]")
        sys.exit(1)
    
    console.print(f"\n[blue]📁 Project to update:[/blue] [bold]{target_path}[/bold]\n")
    
    # Create backup
    backup_dir = target_path / f".speckit-backup-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    backup_dir.mkdir()
    
    # Backup configuration
    tracker_path = target_path / "docs" / "progress-tracker.json"
    if tracker_path.exists():
        shutil.copy(tracker_path, backup_dir / "progress-tracker.json")
    
    constitution_path = target_path / ".specify" / "memory" / "constitution.md"
    if constitution_path.exists():
        shutil.copy(constitution_path, backup_dir / "constitution.md")
    
    console.print(f"[green]✓[/green] Backup created: {backup_dir}")
    
    # Determine what to update
    if not any([update_all, skills, templates, dashboard]):
        update_all = True
    
    # Download and update
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_url = (
            "https://github.com/pravsingh1987/speckit-salesforce.git"
            if use_github else
            "https://git.soma.salesforce.com/praveensingh/speckit-salesforce.git"
        )
        
        console.print("[yellow]Downloading latest SpecKit...[/yellow]")
        result = subprocess.run(
            ["git", "clone", "--depth", "1", repo_url, tmpdir],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            console.print(f"[red]Failed to download: {result.stderr}[/red]")
            sys.exit(1)
        
        tmp_path = Path(tmpdir)
        
        if update_all or skills:
            if (tmp_path / ".cursor" / "skills").exists():
                shutil.rmtree(target_path / ".cursor" / "skills", ignore_errors=True)
                shutil.copytree(tmp_path / ".cursor" / "skills", target_path / ".cursor" / "skills")
                console.print("[green]✓[/green] Updated agent skills")
        
        if update_all or templates:
            if (tmp_path / ".specify" / "templates").exists():
                shutil.rmtree(target_path / ".specify" / "templates", ignore_errors=True)
                shutil.copytree(tmp_path / ".specify" / "templates", target_path / ".specify" / "templates")
                console.print("[green]✓[/green] Updated templates")
        
        if update_all or dashboard:
            if (tmp_path / "docs" / "progress-dashboard.html").exists():
                shutil.copy(tmp_path / "docs" / "progress-dashboard.html", target_path / "docs" / "progress-dashboard.html")
                console.print("[green]✓[/green] Updated dashboard")
    
    # Restore configuration
    if (backup_dir / "progress-tracker.json").exists():
        shutil.copy(backup_dir / "progress-tracker.json", target_path / "docs" / "progress-tracker.json")
        console.print("[green]✓[/green] Restored progress-tracker.json")
    
    rprint("\n[green]✅ Update complete![/green]")
    rprint(f"[dim]Backup location: {backup_dir}[/dim]")
    rprint("\n[yellow]Restart Cursor to use updated skills.[/yellow]")


@main.command()
def version():
    """Show SpecKit version information."""
    table = Table(title="SpecKit Salesforce")
    table.add_column("Component", style="cyan")
    table.add_column("Version", style="green")
    
    table.add_row("SpecKit Salesforce", VERSION)
    table.add_row("Base SpecKit", "0.10.1")
    
    console.print(table)


if __name__ == "__main__":
    main()
