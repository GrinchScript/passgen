# 🔐 PassGen — Smart Password Generator

A minimalist CLI tool to generate cryptographically secure passwords with instant strength check — **zero dependencies**, works 100% offline.

![Demo](demo.gif)

## ✨ Features

- 🔒 **Secure by default** — uses `SystemRandom` (not predictable `random`)
- 🎨 **Colorful output** — visual feedback in terminal
- ⚡ **Strength checker** — instantly rates password (weak/medium/strong)
- 🌐 **No internet required** — your passwords never leave your machine
- 📦 **Zero dependencies** — just Python 3 (preinstalled on most systems)

## 🚀 Quick Start

```bash
git clone https://github.com/GrinchScript/passgen.git
cd passgen
python3 passgen.py
```

## 💡 Usage Examples

```bash
# Default (16 chars, with symbols)
python3 passgen.py

# Custom length (24 chars)
python3 passgen.py -l 24

# Without special characters
python3 passgen.py --no-special
```

## 🔍 Why Offline?

Online password generators *might* log your keystrokes or send data to servers. This tool runs entirely on your machine — no network requests, no tracking, no risk.

## 📦 Requirements

- Python 3.6+ (preinstalled on most Linux/macOS systems)
- No external packages required

---

> Made with ❤️ by [GrinchScript](https://github.com/GrinchScript)
