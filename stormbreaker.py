import os
import sys
import time
import getpass
from modules import utils

PASSWORD = "SH404"

def password_check():
    os.system("clear")
    print("\033[1;91m=== SH404-STORMBREAKER ===\033[0m")
    attempt = getpass.getpass("\033[1;92m[?] Enter Password: \033[0m")
    if attempt != PASSWORD:
        print("\033[1;91m[-] Incorrect password! Exiting...\033[0m")
        sys.exit()
    else:
        utils.print_banner()
        utils.show_disclaimer()
        main_menu()

def main_menu():
    while True:
        print("\n\033[1;94m[ MENU ]\033[0m")
        print("1. Website Recon + Vuln Finder")
        print("2. IP Recon & Scan")
        print("3. Powerful DDoS Attack")
        print("4. SQL Injection Basic")
        print("5. Exit\n")

        choice = input("Choose option [1-5]: ")

        if choice == "1":
            from modules import recon_url
            recon_url.run()
        elif choice == "2":
            from modules import recon_ip
            recon_ip.run()
        elif choice == "3":
            from modules import ddos_attack
            ddos_attack.run()
        elif choice == "4":
            from modules import sql_injector
            sql_injector.run()
        elif choice == "5":
            print("\033[1;92m[✓] Goodbye Vampire Boss!\033[0m")
            sys.exit()
        else:
            print("\033[1;91m[!] Invalid option, try again.\033[0m")

if __name__ == "__main__":
    password_check()
