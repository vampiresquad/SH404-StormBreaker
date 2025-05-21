#!/usr/bin/env python3
import os
import getpass
import sys
import time
from modules import recon_url, recon_ip, ddos, sql_injection, utils

PASSWORD = "SH404"

def slow_print(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def password_prompt():
    try:
        entered = getpass.getpass("\n\033[1;95m[+] Enter Tool Password: \033[0m")
        if entered != PASSWORD:
            print("\033[1;91m[-] Wrong Password! Exiting...\033[0m")
            sys.exit()
    except KeyboardInterrupt:
        print("\n\033[1;91m[!] Interrupted\033[0m")
        sys.exit()

def main_menu():
    os.system("clear")
    utils.print_banner()

    print("\n\033[1;96m===============[ Vampire Web Arsenal ]===============\033[0m")
    print("  \033[1;92m[1]\033[0m Website Recon (URL based)")
    print("  \033[1;92m[2]\033[0m IP Recon")
    print("  \033[1;92m[3]\033[0m High-Power DDoS Attack")
    print("  \033[1;92m[4]\033[0m SQL Injection Module")
    print("  \033[1;91m[99]\033[0m Exit")
    print("\033[1;96m=====================================================\033[0m")

    try:
        choice = input("\n\033[1;93m[?] Select an option: \033[0m").strip()

        if choice == "1":
            recon_url.run()
        elif choice == "2":
            recon_ip.run()
        elif choice == "3":
            ddos.run()
        elif choice == "4":
            sql_injection.run()
        elif choice == "99":
            print("\n\033[1;91m[!] Exiting... Bye Vampire Boss!\033[0m\n")
            sys.exit()
        else:
            print("\033[1;91m[!] Invalid Option!\033[0m")
            time.sleep(1)

        input("\n\033[1;94m[+] Press Enter to return to menu...\033[0m")
        main_menu()
    except KeyboardInterrupt:
        print("\n\n\033[1;91m[!] Interrupted by user\033[0m")

if __name__ == "__main__":
    os.system("clear")
    slow_print("\033[1;95m[•] Welcome to Vampire Web Arsenal...\033[0m", 0.02)
    password_prompt()
    main_menu()
