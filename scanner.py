from netaddr import IPNetwork
import nmap
import json
from datetime import datetime


def generate_ips(cidr):
    try:
        return [str(ip) for ip in IPNetwork(cidr)]
    except Exception as e:
        print("Invalid CIDR format:", e)
        return []


def find_live_hosts(ips):
    nm = nmap.PortScanner()
    live_ips = []

    print("\nScanning for live hosts...\n")

    for ip in ips:
        try:
            result = nm.scan(hosts=ip, arguments='-sn')
            if result['scan']:
                print(f"[+] {ip} is LIVE")
                live_ips.append(ip)
            else:
                print(f"[-] {ip} is DOWN")
        except:
            print(f"[!] Error scanning {ip}")

    return live_ips


def scan_ports(live_ips):
    nm = nmap.PortScanner()
    scan_results = {}

    ports = "21,22,23,25,53,80,110,139,143,443,445,3389"

    print("\nScanning ports...\n")

    for ip in live_ips:
        print(f"Scanning {ip}...")
        open_ports = []

        try:
            nm.scan(ip, ports)

            if ip in nm.all_hosts():
                for proto in nm[ip].all_protocols():
                    for port in nm[ip][proto]:
                        if nm[ip][proto][port]['state'] == 'open':
                            open_ports.append(port)

        except:
            print(f"[!] Error scanning ports for {ip}")

        scan_results[ip] = open_ports

    return scan_results


def save_json(results):
    with open("output.json", "w") as f:
        json.dump(results, f, indent=4)
    print("\nJSON file saved as output.json")


def generate_markdown(results, subnet):
    with open("report.md", "w", encoding="utf-8") as f:
        f.write("# CyberKnight Network Scan Report\n\n")
        f.write(f"Scan Time: {datetime.now()}\n\n")
        f.write(f"Subnet: {subnet}\n\n")

        for ip, ports in results.items():
            f.write(f"## {ip}\n")
            if ports:
                f.write(f"- Open Ports: {ports}\n\n")
            else:
                f.write("- No open ports found\n\n")

    print("Markdown report saved as report.md")


def main():
    subnet = input("Enter CIDR (example: 192.168.1.0/24): ")

    ips = generate_ips(subnet)
    live_ips = find_live_hosts(ips)
    results = scan_ports(live_ips)

    print("\nFinal Results:")
    for ip, ports in results.items():
        print(f"{ip} -> Open Ports: {ports}")

    save_json(results)
    generate_markdown(results, subnet)


if __name__ == "__main__":
    main()