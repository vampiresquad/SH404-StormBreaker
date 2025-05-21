import os
import time
from termcolor import cprint
from pyfiglet import figlet_format

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
