import os
import subprocess
import requests
from modules import utils

def run():
    utils.print_banner()
    utils.notify("IP Reconnaissance Module", "yellow")

    ip = input("\n\033[1;92m[?] Enter IP Address: \033[0m").strip()

    output_dir = ".recon_output/ip_" + ip.replace('.', '_')
    os.makedirs(output_dir, exist_ok=True)

    # 1. GeoIP Information
    utils.notify("Fetching GeoIP Info...", "magenta")
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}")
        data = r.json()
        geo_output = f"""
IP Address   : {ip}
Country      : {data.get('country')}
Region       : {data.get('regionName')}
City         : {data.get('city')}
ISP          : {data.get('isp')}
Org          : {data.get('org')}
AS Number    : {data.get('as')}
Timezone     : {data.get('timezone')}
Lat,Long     : {data.get('lat')}, {data.get('lon')}
        """.strip()

        with open(f"{output_dir}/geoip.txt", "w") as f:
            f.write(geo_output)
        utils.success("GeoIP Info Collected.")
    except Exception as e:
        utils.error(f"GeoIP fetch failed: {str(e)}")

    # 2. Reverse DNS
    utils.notify("Performing Reverse DNS Lookup...", "magenta")
    try:
        revdns = subprocess.check_output(["host", ip], text=True)
        with open(f"{output_dir}/revdns.txt", "w") as f:
            f.write(revdns)
        utils.success("Reverse DNS Lookup Done.")
    except Exception:
        utils.error("Reverse DNS lookup failed.")

    # 3. WHOIS Lookup
    utils.notify("Performing WHOIS Lookup...", "magenta")
    try:
        whois = subprocess.check_output(["whois", ip], text=True)
        with open(f"{output_dir}/whois.txt", "w") as f:
            f.write(whois)
        utils.success("WHOIS Lookup Completed.")
    except Exception:
        utils.error("WHOIS lookup failed.")

    # 4. Port Scanning (Top 1000 TCP ports)
    utils.notify("Scanning Open Ports (nmap)...", "magenta")
    try:
        nmap = subprocess.check_output(["nmap", "-Pn", "-T4", "-F", ip], text=True)
        with open(f"{output_dir}/ports.txt", "w") as f:
            f.write(nmap)
        utils.success("Port Scan Completed.")
    except Exception:
        utils.error("Nmap port scan failed.")

    # 5. Traceroute
    utils.notify("Running Traceroute...", "magenta")
    try:
        trace = subprocess.check_output(["traceroute", ip], text=True)
        with open(f"{output_dir}/traceroute.txt", "w") as f:
            f.write(trace)
        utils.success("Traceroute Completed.")
    except Exception:
        utils.error("Traceroute failed.")

    # 6. Final Output
    print("\n\033[1;94m[+] IP Recon Completed. Results:\033[0m")
    print(f"    GeoIP Info    : {output_dir}/geoip.txt")
    print(f"    Reverse DNS   : {output_dir}/revdns.txt")
    print(f"    Whois         : {output_dir}/whois.txt")
    print(f"    Port Scan     : {output_dir}/ports.txt")
    print(f"    Traceroute    : {output_dir}/traceroute.txt")

    input("\n\033[1;92m[+] Press Enter to return to menu...\033[0m")
