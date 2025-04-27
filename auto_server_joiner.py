import requests
import sys
import os
import time
import random
from colorama import Fore, Style, init

init(autoreset=True)

# ===== ASCII Art =====
ascii_art = r"""
 __ __|       |                          |        _)                    
    |   _ \   |  /   _ \  __ \           |   _ \   |  __ \    _ \   __| 
    |  (   |    <    __/  |   |      \   |  (   |  |  |   |   __/  |    
   _| \___/  _|\_\ \___| _|  _|     \___/  \___/  _| _|  _| \___| _|    
                                                                        
             🚀 Auto Server Joiner - Ryuk.lyy 🚀
"""

print(Fore.CYAN + ascii_art)
print()

# ====== Get Invite Link ======
if len(sys.argv) < 2:
    invite_code = input(Fore.YELLOW + "🔗 Enter the invite link (discord.gg/yourserver): ").strip()
else:
    invite_code = sys.argv[1].strip()

if "discord.gg/" in invite_code:
    invite_code = invite_code.split("discord.gg/")[1]
elif "dsc.gg/" in invite_code:
    invite_code = invite_code.split("dsc.gg/")[1]

# ====== Load tokens ======
tokens_file = "tokens.txt"

if not os.path.exists(tokens_file):
    print(Fore.RED + "❌ tokens.txt file not found! Please add your tokens.")
    input("Press Enter to exit...")
    sys.exit()

with open(tokens_file, "r") as f:
    tokens = [token.strip() for token in f if token.strip()]

# ====== Create results folder ======
os.makedirs("results", exist_ok=True)

success_file = "results/success.txt"
failed_file = "results/failed.txt"

# ====== Ask for delay ======
try:
    delay = float(input(Fore.YELLOW + "⏳ Enter delay between joins (seconds): "))
except ValueError:
    print(Fore.RED + "❌ Invalid delay input. Exiting.")
    sys.exit()

# ====== Fancy loading function ======
def fancy_loading(text):
    loading_symbols = ['|', '/', '-', '\\']
    for _ in range(8):
        for symbol in loading_symbols:
            print(f"\r{Fore.MAGENTA}{text} {symbol}", end='', flush=True)
            time.sleep(0.1)
    print("\r", end='')

# ====== Validate Token ======
def validate_token(token):
    headers = {'Authorization': token}
    res = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
    return res.status_code == 200

# ====== Join Server ======
def join_server(token, invite_code):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': random.choice(user_agents)
    }
    url = f"https://discord.com/api/v9/invites/{invite_code}"
    response = requests.post(url, headers=headers)
    return response

# ====== User agents list ======
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
    "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X)",
]

# ====== Main Process ======
success_count = 0
failed_count = 0

for token in tokens:
    fancy_loading("🔄 Checking token...")
    if not validate_token(token):
        print(Fore.RED + f"❌ Invalid or Locked Token: {token}")
        with open(failed_file, "a") as f:
            f.write(f"Invalid token: {token}\n")
        failed_count += 1
        continue

    fancy_loading("🔄 Joining server...")
    try:
        response = join_server(token, invite_code)
        if response.status_code == 200 or response.status_code == 204:
            print(Fore.GREEN + f"✅ Successfully joined with token: {token}")
            with open(success_file, "a") as f:
                f.write(f"Success: {token}\n")
            success_count += 1
            print('\a')  # Beep sound!
        else:
            error_message = response.json().get('message', 'Unknown Error')
            print(Fore.RED + f"❌ Failed to join: {error_message}")
            with open(failed_file, "a") as f:
                f.write(f"Failed ({error_message}): {token}\n")
            failed_count += 1
    except Exception as e:
        print(Fore.RED + f"❌ Exception occurred: {str(e)}")
        with open(failed_file, "a") as f:
            f.write(f"Exception ({str(e)}): {token}\n")
        failed_count += 1

    time.sleep(delay)

# ====== Final Report ======
print()
print(Fore.CYAN + "=======================================")
print(Fore.CYAN + f"✅ Successful joins: {success_count}")
print(Fore.CYAN + f"❌ Failed joins: {failed_count}")
print(Fore.CYAN + "=======================================")
print(Fore.CYAN + "Made by: Ryuk.lyy")
input(Fore.YELLOW + "\nPress Enter to return to the menu...")
