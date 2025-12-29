# N8N Workflow Backup Automation

Automated backup system for n8n workflows with local cron/systemd scheduling.

## Overview

This automation:
- Fetches all workflows from your local n8n instance every 6 hours
- Detects changes using SHA256 content hashing
- Commits only changed workflows to git
- Pushes changes to GitHub automatically
- Logs all operations for troubleshooting

## Quick Start

### 1. Install the Automation

```bash
cd /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n
./scripts/install_automation.sh
```

This will:
- Install systemd service and timer
- Enable automatic backups every 6 hours
- Start the timer immediately

### 2. Verify Installation

```bash
# Check timer status
systemctl status n8n-backup.timer

# View next scheduled run
systemctl list-timers n8n-backup.timer

# View service logs
journalctl -u n8n-backup.service -f
```

### 3. Test Manually

Before waiting for the scheduled run, test it manually:

```bash
# Dry-run (preview without committing)
./scripts/auto_backup.sh --dry-run

# Actual run (when n8n is running)
./scripts/auto_backup.sh

# Or trigger via systemd
sudo systemctl start n8n-backup.service
```

## Configuration

### Update n8n URL or API Token

Edit the service file:

```bash
sudo nano /etc/systemd/system/n8n-backup.service
```

Update these lines:
```ini
Environment="N8N_API_URL=http://localhost:5678"
Environment="N8N_API_TOKEN=your_token_here"
```

Then reload:
```bash
sudo systemctl daemon-reload
sudo systemctl restart n8n-backup.timer
```

### Change Backup Schedule

Edit the timer file:

```bash
sudo nano /etc/systemd/system/n8n-backup.timer
```

Examples:
```ini
# Every 4 hours
OnCalendar=*-*-* 00,04,08,12,16,20:00:00

# Every 12 hours
OnCalendar=*-*-* 00,12:00:00

# Daily at 2 AM
OnCalendar=*-*-* 02:00:00
```

Then reload:
```bash
sudo systemctl daemon-reload
sudo systemctl restart n8n-backup.timer
```

## Management Commands

### Timer Control

```bash
# Start timer (enable automatic backups)
sudo systemctl start n8n-backup.timer

# Stop timer (disable automatic backups)
sudo systemctl stop n8n-backup.timer

# Enable timer on boot
sudo systemctl enable n8n-backup.timer

# Disable timer on boot
sudo systemctl disable n8n-backup.timer
```

### Manual Backup

```bash
# Trigger immediate backup
sudo systemctl start n8n-backup.service

# Dry-run (preview changes)
./scripts/auto_backup.sh --dry-run

# Run directly
./scripts/auto_backup.sh
```

### Logs and Monitoring

```bash
# Follow service logs in real-time
journalctl -u n8n-backup.service -f

# View recent logs
journalctl -u n8n-backup.service -n 50

# View timer logs
journalctl -u n8n-backup.timer -n 20

# Check script log file
tail -f /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/auto_backup.log
```

## Troubleshooting

### n8n not responding

**Error**: `n8n is not responding at http://localhost:5678`

**Solutions**:
1. Check if n8n is running: `curl http://localhost:5678/healthz`
2. Verify n8n port: `ss -tulpn | grep 5678`
3. Check n8n service: `docker ps | grep n8n` or `systemctl status n8n`

### API authentication failed

**Error**: `401 Unauthorized` or `403 Forbidden`

**Solutions**:
1. Regenerate API token in n8n: Settings → API → Generate new token
2. Update token in service file: `sudo nano /etc/systemd/system/n8n-backup.service`
3. Reload: `sudo systemctl daemon-reload && sudo systemctl restart n8n-backup.timer`

### Git push fails

**Error**: `Failed to push changes`

**Solutions**:
1. Check git credentials: `git config --list | grep credential`
2. Set up SSH keys for GitHub: `ssh -T git@github.com`
3. Or use credential helper: `git config --global credential.helper store`

### No changes detected

**Info**: `Backup completed (no changes)`

This is normal when workflows haven't been modified. The automation only commits actual changes to reduce git noise.

## Files and Locations

```
/home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n/
├── scripts/
│   ├── auto_backup.sh              # Main backup script
│   ├── fetch_n8n_workflows.py      # n8n API fetcher
│   ├── install_automation.sh       # Systemd installer
│   ├── n8n-backup.service          # Systemd service
│   └── n8n-backup.timer            # Systemd timer
├── workflow_backups/               # Categorized workflows
├── auto_backup.log                 # Script log file
└── AUTOMATION_SETUP.md             # This file

/etc/systemd/system/
├── n8n-backup.service              # Installed service
└── n8n-backup.timer                # Installed timer
```

## Alternative: Cron Setup

If you prefer cron over systemd:

```bash
# Open crontab
crontab -e

# Add this line (runs every 6 hours)
0 */6 * * * cd /home/rohi/homelab/swarm/stacks/04-n8n/n8n-repos/n8n && ./scripts/auto_backup.sh >> auto_backup.log 2>&1
```

## Uninstall

To remove the automation:

```bash
# Stop and disable timer
sudo systemctl stop n8n-backup.timer
sudo systemctl disable n8n-backup.timer

# Remove service files
sudo rm /etc/systemd/system/n8n-backup.service
sudo rm /etc/systemd/system/n8n-backup.timer

# Reload systemd
sudo systemctl daemon-reload
```

The script files in `scripts/` and workflow backups are not removed, so you can reinstall later if needed.

## How It Works

1. **Timer triggers** at scheduled intervals (default: every 6 hours)
2. **Service executes** `auto_backup.sh` script
3. **Script checks** if n8n is running and accessible
4. **Fetches workflows** via n8n API using `fetch_n8n_workflows.py`
5. **Detects changes** by computing SHA256 hash of workflow content
6. **Updates catalog** with `catalog_workflows.py`
7. **Commits changes** if any workflows were modified
8. **Pushes to GitHub** automatically
9. **Logs everything** to `auto_backup.log` and systemd journal

## Security Notes

- API token is stored in systemd service file (readable only by root and your user)
- Consider using environment file for sensitive data: `/etc/default/n8n-backup`
- Enable 2FA on your GitHub account
- Use SSH keys instead of HTTPS for git push (more secure)

## Support

For issues or questions:
1. Check logs: `journalctl -u n8n-backup.service -n 100`
2. Test manually: `./scripts/auto_backup.sh --dry-run`
3. Verify n8n API: `curl http://localhost:5678/api/v1/workflows -H "X-N8N-API-KEY: your_token"`
