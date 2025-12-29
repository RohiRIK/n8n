#!/bin/bash
#
# N8N Backup Automation Installer
# Installs systemd timer for automated workflow backups
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SERVICE_FILE="$SCRIPT_DIR/n8n-backup.service"
TIMER_FILE="$SCRIPT_DIR/n8n-backup.timer"

echo "=== N8N Backup Automation Installer ==="
echo ""

# Check if running as root
if [ "$EUID" -eq 0 ]; then
  echo "ERROR: Do not run this script as root"
  echo "Run it as your regular user, and you'll be prompted for sudo when needed"
  exit 1
fi

# Check if systemd is available
if ! command -v systemctl &> /dev/null; then
  echo "ERROR: systemd is not available on this system"
  echo "Please use cron instead. Add this to your crontab:"
  echo ""
  echo "  0 */6 * * * cd $SCRIPT_DIR/.. && $SCRIPT_DIR/auto_backup.sh >> $SCRIPT_DIR/../auto_backup.log 2>&1"
  echo ""
  exit 1
fi

# Check if service files exist
if [ ! -f "$SERVICE_FILE" ] || [ ! -f "$TIMER_FILE" ]; then
  echo "ERROR: Service files not found"
  echo "Expected files:"
  echo "  - $SERVICE_FILE"
  echo "  - $TIMER_FILE"
  exit 1
fi

echo "Installing systemd service and timer..."
echo ""

# Copy service files to systemd directory
sudo cp -v "$SERVICE_FILE" /etc/systemd/system/
sudo cp -v "$TIMER_FILE" /etc/systemd/system/

# Reload systemd daemon
echo ""
echo "Reloading systemd daemon..."
sudo systemctl daemon-reload

# Enable and start timer
echo "Enabling n8n-backup.timer..."
sudo systemctl enable n8n-backup.timer

echo "Starting n8n-backup.timer..."
sudo systemctl start n8n-backup.timer

# Show status
echo ""
echo "=== Installation Complete ==="
echo ""
echo "Timer status:"
sudo systemctl status n8n-backup.timer --no-pager

echo ""
echo "Next scheduled run:"
systemctl list-timers n8n-backup.timer --no-pager

echo ""
echo "=== Useful Commands ==="
echo "  View timer status:        systemctl status n8n-backup.timer"
echo "  View service logs:        journalctl -u n8n-backup.service -f"
echo "  View next scheduled run:  systemctl list-timers n8n-backup.timer"
echo "  Trigger backup manually:  sudo systemctl start n8n-backup.service"
echo "  Stop automation:          sudo systemctl stop n8n-backup.timer"
echo "  Disable automation:       sudo systemctl disable n8n-backup.timer"
echo ""
