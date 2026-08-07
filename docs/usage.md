# Usage (Kali Linux)

1. Install Python dependencies:
   sudo apt update
   sudo apt install -y python3 python3-pip
   pip3 install -r requirements.txt

2. Install recommended scanners (on Kali many are preinstalled):
   sudo apt install -y nmap nikto dirb sqlmap docker.io

3. Dry-run example:
   python3 tools/cli.py --target example.com

4. To execute (DANGEROUS — only with authorization):
   - Create an authorization file from `auth-template.txt` and store it locally.
   - Set environment variable: export ALLOW_EXECUTION=1
   - Run:
     python3 tools/cli.py --target example.com --execute --auth-file /path/to/auth.txt

5. Reports are saved to the `results/` directory by default.

Always confirm authorization before executing real scans.
