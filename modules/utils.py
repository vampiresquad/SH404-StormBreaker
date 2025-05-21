import os
import time
from termcolor import cprint
from pyfiglet import figlet_format
import shutil

def print_banner():
    os.system("clear")
    banner = r'''
\033[1;91m
██╗   ██╗ █████╗ ███╗   ███╗██████╗ ██╗██████╗ ███████╗
██║   ██║██╔══██╗████╗ ████║██╔══██╗██║██╔══██╗██╔════╝
██║   ██║███████║██╔████╔██║██████╔╝██║██║  ██║█████╗  
╚██╗ ██╔╝██╔══██║██║╚██╔╝██║██╔═══╝ ██║██║  ██║██╔══╝  
 ╚████╔╝ ██║  ██║██║ ╚═╝ ██║██║     ██║██████╔╝███████╗
  ╚═══╝  ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚═════╝ ╚══════╝
       \033[1;97m=> Coded By: Muhammad Shourov (VAMPIRE)
'''
    print(banner)

def notify(msg, color="green"):
    colors = {"red": "91", "green": "92", "blue": "94", "yellow": "93"}
    print(f"\n\033[1;{colors.get(color,'92')}m[+]\033[0m \033[1m{msg}\033[0m")

def error(msg):
    print(f"\033[1;91m[-] Error: {msg}\033[0m")

def warn(msg):
    print(f"\033[1;93m[!] {msg}\033[0m")

def success(msg):
    print(f"\033[1;92m[✓] {msg}\033[0m")

def check_tool(name):
    return shutil.which(name)

def install_tool(name):
    print(f"\033[1;94m[+] Installing {name}...\033[0m")
    os.system(f"pkg install {name} -y || apt install {name} -y || apt-get install {name} -y")

def print_banner():
    os.system("clear")
    cprint(figlet_format('SH404', font='slant'), 'red', attrs=['bold'])
    print("\033[1;92m[+] Tool   : SH404-StormBreaker")
    print("[+] Coder  : Muhammad Shourov (Vampire)")
    print("[+] Power  : Real-time Recon | DDoS | SQLi\033[0m")
    print("-" * 50)

def show_disclaimer():
    print("\033[1;93m[!] Disclaimer:")
    print("    This tool is only for educational and authorized use.")
    print("    Use it at your own risk. The developer holds no responsibility.")
    print("-" * 50)
    time.sleep(2)

def notify(text, color="cyan"):
    cprint(f"[~] {text}", color)

def success(text):
    cprint(f"[✓] {text}", "green")

def error(text):
    cprint(f"[✗] {text}", "red")

def wait(seconds):
    time.sleep(seconds)
