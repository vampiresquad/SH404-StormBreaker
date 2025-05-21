#!/bin/bash

clear
echo -e "\e[1;91m[+] Starting SH404-StormBreaker Installer...\e[0m"

# Fix storage issue in Termux (if needed)
termux-setup-storage &> /dev/null

# Internet check
ping -c 1 google.com &>/dev/null
if [ $? -ne 0 ]; then
    echo -e "\e[1;91m[-] No internet connection. Please connect to the internet!\e[0m"
    exit 1
fi

# Install/update Python & dependencies
echo -e "\e[1;92m[*] Installing packages...\e[0m"
pkg update -y && pkg upgrade -y
pkg install python git curl wget openssh -y

# Handle pip install issue (Termux special fix)
if ! command -v pip &> /dev/null; then
    echo -e "\e[1;93m[*] pip not found, attempting fix...\e[0m"
    pkg install python-pip -y || apt install python3-pip -y
    pip install --upgrade pip --break-system-packages
fi

# Install required Python modules
echo -e "\e[1;92m[*] Installing Python dependencies...\e[0m"
pip install -r requirements.txt --break-system-packages

# Install Nikto manually if needed
if ! command -v nikto &> /dev/null; then
    echo -e "\e[1;93m[*] Nikto not found. Installing...\e[0m"
    git clone https://github.com/sullo/nikto.git tools/nikto
    ln -s $PWD/tools/nikto/program/nikto.pl /data/data/com.termux/files/usr/bin/nikto
    chmod +x /data/data/com.termux/files/usr/bin/nikto
fi

# Install Nmap if missing
if ! command -v nmap &> /dev/null; then
    pkg install nmap -y
fi

echo -e "\e[1;92m[✓] All dependencies installed successfully!\e[0m"
echo -e "\e[1;96m[>] You can now run: python stormbreaker.py\e[0m"
