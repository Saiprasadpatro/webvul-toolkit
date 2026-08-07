# Contributing

Please read carefully — this project is security-sensitive.

Responsible disclosure
- If you find a vulnerability in this toolkit (or discover the toolkit could be misused), open an issue marked `security` or email the repo owner with details.
- Do NOT publish PoCs that enable misuse without prior consent.

Adding scanners
- Keep dry-run the default behavior.
- Add any scanner command templates in `tools/cli.py` and document required binaries or Docker images in `config/example.yaml`.

Testing
- Provide unit tests for command generation and authorization checks.
- CI runs linting and tests only; it does NOT execute scanners.

Code of conduct
- Be professional and respect legal and ethical boundaries when using or contributing to this toolkit.
