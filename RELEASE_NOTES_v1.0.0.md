# 🚀 Webvul-Toolkit v1.0.0 Release

![Ethical Bug Bounty Toolkit](https://img.shields.io/badge/Security-Toolkit-brightgreen?style=for-the-badge&logo=python)

## Overview
Webvul-Toolkit v1.0.0 marks the **first stable release** of an ethical, security-focused CLI wrapper designed to orchestrate common open-source security scanners for authorized penetration testing and bug bounty work.

---

## ✨ Key Features

### 🔒 Safety-First Approach
- **Dry-run by default** — Preview all scanner commands before execution
- **Explicit authorization required** — Execute mode needs environment variable + auth file verification
- **Built-in safeguards** — Local file validation on authorization before any scanning occurs

### 🛠️ Integrated Security Scanners
- **nmap** — Network reconnaissance and port scanning
- **nikto** — Web server vulnerability scanning
- **dirb** — Directory enumeration and brute-forcing
- **sqlmap** — SQL injection detection and exploitation
- **OWASP ZAP** — Comprehensive web application security testing (Docker support)

### 📋 CLI Interface
- Simple, intuitive command-line interface
- YAML-based configuration support
- Per-target scanner customization
- Extensible architecture for adding new scanners

### ✅ Quality Assurance
- Basic CI/CD pipeline with linting and testing
- Contributing guidelines for responsible disclosure
- MIT License for open-source collaboration

---

## 🎯 Quick Start

### Installation
```bash
pip3 install -r requirements.txt
```

### Dry-Run (Default)
```bash
python3 tools/cli.py --target example.com
```
This safely previews all scanner commands without executing them.

### Authorized Execution
```bash
export ALLOW_EXECUTION=1
python3 tools/cli.py --target example.com --execute --auth-file /path/to/auth.txt
```

---

## 📦 What's Included

| File | Purpose |
|------|---------|
| `tools/cli.py` | Safe Python CLI wrapper with dry-run defaults |
| `config/example.yaml` | Example scanner configuration |
| `docs/usage.md` | Detailed setup & usage for Kali Linux |
| `.github/workflows/basic-ci.yml` | Automated linting and testing |
| `CONTRIBUTING.md` | Responsible disclosure guidelines |
| `LICENSE` | MIT License |

---

## ⚖️ Legal & Ethical Guidelines

**IMPORTANT:** This toolkit is designed for authorized security testing only.

### You must have explicit written authorization to:
- Test any system or network
- Perform vulnerability scanning
- Conduct penetration testing
- Run this toolkit against any target

### By using this toolkit, you affirm:
- ✅ You have written authorization from the asset owner
- ✅ Testing is limited to authorized targets (bug bounty programs, your own assets, etc.)
- ✅ You understand the legal implications of unauthorized testing

**⚠️ The author (Saiprasadpatro) is NOT responsible for misuse.**

---

## 🚀 Getting Started

1. **Review** `docs/usage.md` for platform-specific setup instructions
2. **Configure** your scanners using `config/example.yaml` as a template
3. **Test dry-run** with your authorized target
4. **Enable execution** only when fully authorized and confident
5. **Contribute** improvements via PRs (see `CONTRIBUTING.md`)

---

## 📚 Documentation

- **[Usage Guide](docs/usage.md)** — Setup and running on Kali Linux
- **[Contributing Guidelines](CONTRIBUTING.md)** — How to contribute responsibly
- **[Configuration Example](config/example.yaml)** — Scanner configuration template

---

## 🔄 Release Highlights

### v1.0.0 Stable Release
- ✅ Core CLI wrapper with dry-run safety defaults
- ✅ Support for 5 major security scanners (nmap, nikto, dirb, sqlmap, OWASP ZAP)
- ✅ Authorization framework with file validation
- ✅ CI/CD pipeline and testing infrastructure
- ✅ Comprehensive documentation and contributing guidelines
- ✅ MIT License for community collaboration

---

## 🤝 Contributing

We welcome contributions that enhance security testing capabilities while maintaining our safety-first ethos. Please:

1. Read `CONTRIBUTING.md` for guidelines
2. Ensure your addition includes authorization checks
3. Test your scanner integration thoroughly
4. Submit a PR with clear documentation

---

## 📄 License

This project is released under the **MIT License**. See `LICENSE` file for details.

---

## 📞 Support

- Report issues via GitHub Issues
- Check existing documentation in `docs/`
- Follow responsible disclosure practices
- Review contributing guidelines before submitting PRs

---

**Built with ❤️ for ethical security testing.**

*Remember: With great power comes great responsibility. Always get explicit authorization before testing.*

---

*Release Date: August 7, 2026*  
*Python 100% | MIT License | Open Source*