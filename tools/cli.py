#!/usr/bin/env python3
"""
Safe Bug Bounty Toolkit CLI (DRY-RUN by default).

Prints the commands that would run for the specified scanners.
To actually run commands, pass --execute, provide --auth-file pointing to a
local authorization file, and set the environment variable
ALLOW_EXECUTION=1.

Use only against targets you are explicitly authorized to test.
"""

import argparse
import os
import sys
import yaml
import subprocess
from datetime import datetime
from shutil import which

ROOT = os.path.dirname(os.path.dirname(__file__))

DEFAULT_CONFIG = os.path.join(ROOT, "config", "example.yaml")

SCANNER_COMMANDS = {
    "nmap": "nmap -sV -A {target} -oN {outfile}",
    "nikto": "nikto -h {target} -output {outfile}",
    "dirb": "dirb http://{target} -o {outfile}",
    "sqlmap": "sqlmap -u {target} --batch --output-dir={outdir}",
    "zap": (
        "docker run --rm owasp/zap2docker-stable "
        "zap-baseline.py -t {target} -r {outfile}.html"
    ),
}


def load_config(path):
    """Load YAML configuration from path.

    Returns the parsed config or raises on error.
    """
    with open(path, "r") as f:
        return yaml.safe_load(f)


def check_auth_file(path):
    """Return True if path is a valid existing file.

    The CLI requires a local authorization file before executing scanners.
    """
    return bool(path and os.path.isfile(path))


def ensure_outdir(path):
    """Create the output directory if it does not exist.

    Returns the path for convenience.
    """
    os.makedirs(path, exist_ok=True)
    return path


def build_commands(target, scanners, outdir, config=None):
    """Build scanner command strings for the provided target.

    Returns a list of tuples: (scanner_name, command_string).
    """
    ts = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    cmds = []

    for s in scanners:
        # Prefer config templates if provided.
        templ = None
        if config and "scanners" in config:
            for entry in config["scanners"]:
                if entry.get("name") == s:
                    templ = entry.get("command_template")
                    break

        if not templ:
            templ = SCANNER_COMMANDS.get(s)

        if not templ:
            continue

        name_safe = target.replace(":", "_")
        fname = f"{s}_{name_safe}_{ts}.txt"
        outfile = os.path.join(outdir, fname)

        cmd = templ.format(target=target, outdir=outdir, outfile=outfile)
        cmds.append((s, cmd))

    return cmds


def main():
    p = argparse.ArgumentParser(
        description=(
            "Ethical Bug Bounty Toolkit (DRY-RUN by default)."
        )
    )

    p.add_argument(
        "--target",
        required=True,
        help="Target hostname or IP (AUTHORIZED ONLY).",
    )

    p.add_argument(
        "--scanners",
        nargs="+",
        choices=list(SCANNER_COMMANDS.keys()),
        default=["nmap", "nikto", "dirb", "sqlmap", "zap"],
        help="List of scanners to include.",
    )

    p.add_argument(
        "--config",
        default=DEFAULT_CONFIG,
        help="Path to scanner config YAML.",
    )

    p.add_argument(
        "--outdir",
        default="results",
        help="Directory to write report files.",
    )

    p.add_argument(
        "--auth-file",
        default="",
        help=(
            "Path to authorization proof file required to execute scans."
        ),
    )

    p.add_argument(
        "--execute",
        action="store_true",
        help=(
            "If set, attempt to execute commands (requires auth-file "
            "and ALLOW_EXECUTION=1)."
        ),
    )

    args = p.parse_args()

    config = None
    if os.path.isfile(args.config):
        try:
            config = load_config(args.config)
        except Exception:
            print(
                "Warning: failed to parse config; falling back to "
                "built-in templates."
            )

    outdir = ensure_outdir(args.outdir)
    cmds = build_commands(args.target, args.scanners, outdir, config)

    print("== Ethical Bug Bounty Toolkit ==")
    print("Target:", args.target)
    print("Scanners:", ", ".join([s for s, _ in cmds]))
    print("Output dir:", outdir)
    print()

    if not cmds:
        print("No commands available for selected scanners.")
        sys.exit(1)

    if not args.execute:
        print("[DRY-RUN] Commands that would be executed:")
        for s, c in cmds:
            print(f"  [{s}] {c}")
        sys.exit(0)

    # Execution path - guarded
    if not check_auth_file(args.auth_file):
        print(
            "ERROR: Execution requires a valid --auth-file path pointing to "
            "a local authorization document."
        )
        sys.exit(2)

    if os.environ.get("ALLOW_EXECUTION") != "1":
        print(
            "ERROR: To execute commands you must set ALLOW_EXECUTION=1 "
            "in the environment (extra safeguard)."
        )
        sys.exit(3)

    print("Authorization file found and ALLOW_EXECUTION=1 — executing commands now.")

    for s, c in cmds:
        print(f"Running [{s}]: {c}")
        try:
            # Use shell=True intentionally for command templates that may be
            # provided as full shell strings; ensure inputs are trusted.
            result = subprocess.run(c, shell=True)
            if result.returncode != 0:
                print(f"[{s}] exited with code {result.returncode}")
        except Exception as e:
            print(f"[{s}] execution failed: {e}")

    print("Execution finished. Check", outdir)


if __name__ == "__main__":
    main()
