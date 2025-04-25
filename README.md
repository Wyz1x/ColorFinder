# 🎨 ColorFinder

**ColorFinder** is a simple Python script that automatically fetches and extracts all colors from a website's CSS. It supports HEX, RGB(A), and HSL(A) formats.

---

## 🚀 Features

- Downloads and parses the website’s CSS
- Finds all used colors in styles
- Supports the following color formats:
  - `#HEX`
  - `rgb()`, `rgba()`
  - `hsl()`, `hsla()`
- Outputs all unique colors
- Deletes the temporary CSS file after parsing

---

## 🧰 Installation
#### Windows
Install Python3
Install the project from this repository

CD to project path and run this command:
```bash
pip install -r requirements.txt
```
#### linux/macOS
```bash
apt update && apt upgrade -y
apt install python
apt install git
git clone https://github.com/Wyz1x/ColorFinder.git
cd ColorFinder
pip install -r requirements.txt
```
or

```bash
brew update
brew install python
brew install git
git clone https://github.com/Wyz1x/ColorFinder.git
cd ColorFinder
pip3 install -r requirements.txt
```
#### If you using Homebrew
---
## ⌨️Using
Windows/Linux/MacOS
CD to project path and run this command:
```bash
python3 main.py
```
CD:
```bash
cd projectPath
