# Ethical Bug Bounty Toolkit

Purpose
- A safe, ethical CLI wrapper to orchestrate common open-source security scanners (nmap, nikto, dirb, sqlmap, OWASP ZAP).
- Intended to be run only against targets you are explicitly authorized to test (bug-bounty targets, your own assets, or with written permission).
- Dry-run by default. Execution requires explicit authorization and an environment variable to be set.

Disclaimer / Legal
- Do NOT use this toolkit to test systems without explicit, written authorization from the asset owner.
- The author (Saiprasadpatro) is NOT responsible for misuse. By using this toolkit you affirm you have authorization to test the specified target(s).

Contents
- tools/cli.py — Safe Python CLI wrapper (dry-run default).
- config/example.yaml — Example configuration for scanners.
- docs/usage.md — Setup and usage instructions for Kali Linux.
- .github/workflows/basic-ci.yml — Basic lint/test workflow.
- CONTRIBUTING.md — Responsible disclosure and contribution guidelines.
- LICENSE — MIT.

Quick start (dry-run)
1. Install dependencies:
   pip3 install -r requirements.txt
2. Run a dry-run:
   python3 tools/cli.py --target example.com
   This prints the scanner commands that would be run.

Enabling actual execution (strong safeguards)
- To allow the CLI to execute commands (not recommended until you fully understand and have authorization):
  1. Create an authorization file (see auth-template.txt) signed/approved by the target owner.
  2. Set environment variable: export ALLOW_EXECUTION=1
  3. Run with --execute and --auth-file /path/to/auth.txt
- The script still performs a local file check on --auth-file before executing.

Recommended scanners included
- nmap, nikto, dirb, sqlmap, OWASP ZAP (via docker). The wrapper can be extended to include other tools.

Support & Contribution
- Follow the contributing guidelines in CONTRIBUTING.md.
- Open PRs for new scanner modules, but ensure each addition keeps the safety-first defaults.
