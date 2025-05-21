import os
import subprocess
from modules import utils

def run():
    utils.print_banner()
    utils.notify("Website Recon + Parameter-based Vulnerability Scan", "yellow")

    url = input("\n\033[1;92m[?] Enter Website URL (https://example.com): \033[0m").strip()

    if not url.startswith("http"):
        url = "https://" + url

    utils.notify(f"Target: {url}", "cyan")

    output_dir = ".recon_output"
    os.makedirs(output_dir, exist_ok=True)

    # 1. Subdomain Enumeration
    utils.notify("Running subfinder (if installed)...", "magenta")
    try:
        subdomains = subprocess.check_output(["subfinder", "-d", url.replace("https://", "").replace("http://", ""), "-silent"], text=True)
        with open(f"{output_dir}/subdomains.txt", "w") as f:
            f.write(subdomains)
        utils.success(f"Subdomains Found: {len(subdomains.strip().splitlines())}")
    except Exception:
        utils.error("Subfinder not found or failed.")

    # 2. Wayback URL Collection
    utils.notify("Collecting Wayback URLs...", "magenta")
    try:
        wayback = subprocess.check_output(["waybackurls", url], text=True)
        with open(f"{output_dir}/waybackurls.txt", "w") as f:
            f.write(wayback)
        utils.success(f"Wayback URLs Collected: {len(wayback.strip().splitlines())}")
    except Exception:
        utils.error("waybackurls not found or failed.")

    # 3. Parameter Discovery
    utils.notify("Finding URLs with parameters...", "magenta")
    param_urls = []
    try:
        with open(f"{output_dir}/waybackurls.txt", "r") as f:
            for line in f:
                if "?" in line and "=" in line:
                    param_urls.append(line.strip())

        with open(f"{output_dir}/param_urls.txt", "w") as f:
            for url in param_urls:
                f.write(url + "\n")

        utils.success(f"Parameter URLs Found: {len(param_urls)}")

    except FileNotFoundError:
        utils.error("Wayback file missing.")

    # 4. Vuln Checking via GF (if available)
    gf_vulns = {}
    gf_patterns = {
        "xss": "xss",
        "sqli": "sqli",
        "ssrf": "ssrf",
        "rce": "rce"
    }

    for vuln, gf_pattern in gf_patterns.items():
        utils.notify(f"Checking for {vuln.upper()} parameters using GF...", "blue")
        try:
            result = subprocess.check_output(f"cat {output_dir}/param_urls.txt | gf {gf_pattern}", shell=True, text=True)
            lines = result.strip().splitlines()
            if lines:
                gf_vulns[vuln] = lines
                with open(f"{output_dir}/{vuln}_params.txt", "w") as f:
                    f.write("\n".join(lines))
                utils.success(f"{vuln.upper()} params found: {len(lines)}")
            else:
                utils.notify(f"No {vuln.upper()} params found.", "white")
        except Exception:
            utils.error(f"GF not found or failed for {vuln.upper()}")

    # 5. Final Output
    print("\n\033[1;94m[+] Recon Completed. Results:\033[0m")
    print(f"    Subdomains    : {output_dir}/subdomains.txt")
    print(f"    Wayback URLs  : {output_dir}/waybackurls.txt")
    print(f"    Param URLs    : {output_dir}/param_urls.txt")
    for vuln, _ in gf_vulns.items():
        print(f"    {vuln.upper()} URLs : {output_dir}/{vuln}_params.txt")

    input("\n\033[1;92m[+] Press Enter to return to menu...\033[0m")
