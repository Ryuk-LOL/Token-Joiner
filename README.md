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

- 2. Install dependencies:
Make sure you have Python 3 installed on your system. Install the required library colorama for colored text:


pip install colorama
3. Setup Tokens:
Create a tokens.txt file in the project folder, where each line should contain a valid Discord token.

4. Start the Program:
Run the start_joiner.bat file. This will launch a clean Command Prompt menu.


start_joiner.bat
🔧 How It Works
Menu: The program will prompt you with a menu. Select 1 to start the token joining process or 2 to exit.

Invite Code: Enter the Discord invite link (e.g., discord.gg/yourserver).

Token Processing: The program will automatically validate each token, trying to join the server with each one.

Result: After the process is finished, the program will display a report showing how many successful joins and failed attempts there were. The results will also be saved in results/success.txt and results/failed.txt.

📂 Folder Structure

AutoServerJoiner/
│
├── auto_server_joiner.py      # Main Python script for joining servers
├── start_joiner.bat           # Batch file to start the tool
├── tokens.txt                 # Your Discord tokens
├── proxies.txt (optional)    # Proxy list (if needed)
└── results/                   # Folder where success and failed joins are saved
    ├── success.txt            # Tokens that successfully joined the server
    └── failed.txt             # Tokens that failed to join (invalid, locked)
⚡ Commands & Options
1. Token Joiner: Starts the process to join the server with tokens.

2. Exit: Exits the program.

Features While Running
🔄: Loading icon while processing each token.

✅: Successfully joined message for each token.

❌: Failed join message for invalid tokens or errors.

🧠 Important Notes
For Educational Purposes: This tool is only for educational purposes. Use responsibly and avoid violating Discord's Terms of Service.

Token Limits: Discord limits how many servers a token can join. If the token is already in many servers, it may not be able to join more.

Rate-Limiting: Always use a delay between joins (suggested delay: 3-5 seconds).

🚨 Warning
Please ensure you're not violating any terms or conditions while using this tool. Discord may ban accounts that engage in suspicious activity, so always use caution!

📈 Future Updates (Planned Features)
🌍 Proxy support to hide your IP address when joining servers.

🌐 More advanced user-agent rotation to simulate different devices and browsers.

🔑 Auto-detect and remove banned tokens from tokens.txt.

👨‍💻 Made By
Ryuk.lyy

Feel free to fork, modify, and improve the project. Contributions are welcome!

## 🛠 **Installation**

### 1. **Clone the repository** or download the zip file:
```bash
git clone https://github.com/yourusername/AutoServerJoiner.git
