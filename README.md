# Token-Joiner

# 🚀 **Auto Server Joiner** - Made by Ryuk.lyy

![License](https://img.shields.io/github/license/Ryuk-LOL/Token-Joiner?color=blue)
![Version](https://img.shields.io/badge/version-1.0-green)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Stars](https://img.shields.io/github/stars/Ryuk-LOL/Token-Joiner?style=social)

Welcome to **Auto Server Joiner**, a tool for joining Discord servers using tokens! This tool allows you to join a Discord server by simply providing an invite link and a list of tokens. It will automatically validate each token, join the server, and provide a detailed report with success and failure logs.

## 🎯 **Features**
- 📝 **Token Validation**: Automatically checks if each token is valid or locked before trying to join.
- ✅ **Success Log**: Saves all successful joins in a `success.txt` file.
- ❌ **Failure Log**: Saves failed joins (invalid tokens, errors) in a `failed.txt` file.
- 🕹 **Menu Interface**: A clean command-line menu where you can select options.
- 🐣 **Automatic Invite Code Handling**: Simply provide a Discord invite link to start the joining process.
- ⏳ **Custom Delay**: Set a delay between each join to avoid rate-limiting or spam detection.
- 🎶 **Sound Effects**: Plays a beep sound when a token successfully joins a server.
- 🎨 **Emoji Updates**: Uses emojis to indicate status:
  - ✅ for successful joins
  - ❌ for failed joins
  - 🔄 for loading states
- 🧑‍💻 **User-Agent Rotation**: Randomly rotates user-agent headers to mimic different browsers.

## 🛠 **Installation**

### 1. **Clone the repository** or download the zip file:
```bash
git clone https://github.com/yourusername/AutoServerJoiner.git
