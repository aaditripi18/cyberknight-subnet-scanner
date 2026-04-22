# 🛡️ CyberKnight CIDR Subnet Scanner

## 📌 Overview

This project is a **Python-based network scanning tool** that accepts a CIDR subnet as input, identifies live hosts, performs port scanning, and generates structured outputs in both **JSON** and **Markdown** formats.

The tool leverages **Nmap** for accurate network discovery and is designed to be simple, efficient, and easy to deploy using Docker.

---

## 🚀 Features

* 🔍 **CIDR Subnet Scanning**
  Generate all IP addresses within a given subnet range.

* 🌐 **Live Host Detection**
  Identify active hosts using Nmap ping scan.

* 🔓 **Port Scanning**
  Scan common ports on all live hosts.

* 📄 **JSON Output**
  Machine-readable output of IPs and open ports.

* 📝 **Markdown Report**
  Clean, human-readable report for analysis.

* 🐳 **Docker Support**
  Run the entire application in an isolated container.

---

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:**

  * python-nmap
  * netaddr
  * tqdm
* **Tool:** Nmap
* **Containerization:** Docker

---

## 📂 Project Structure

```
cyberknight-subnet-scanner/
│
├── scanner.py        # Main application script
├── requirements.txt  # Python dependencies
├── Dockerfile        # Docker configuration
├── README.md         # Documentation
├── output.json       # Generated JSON output
└── report.md         # Generated Markdown report
```

---

## ⚙️ Installation

### 🔹 1. Clone the Repository

```bash
git clone https://github.com/aaditripi18/cyberknight-subnet-scanner.git
cd cyberknight-subnet-scanner
```

---

### 🔹 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

### 🔹 3. Install Nmap

Download and install from:
👉 https://nmap.org/download.html

⚠️ Ensure Nmap is added to your system PATH.

---

## ▶️ Usage

Run the script:

```bash
python scanner.py
```

Enter a CIDR subnet when prompted:

```bash
192.168.1.0/24
```

---

## 🧪 Example Run

### 🔹 Input

```
127.0.0.1/32
```

### 🔹 Output (Terminal)

```
Scanning for live hosts...

[+] 127.0.0.1 is LIVE

Scanning ports...

127.0.0.1 -> Open Ports: [445]
```

---

## 📄 Output Files

### 🔹 JSON Output (`output.json`)

```json
{
    "127.0.0.1": [445]
}
```

---

### 🔹 Markdown Report (`report.md`)

Includes:

* Scan time
* Subnet scanned
* List of live IPs
* Open ports per IP

---

## ⚙️ Code Structure

The main script `scanner.py` is organized into modular functions:

* **`generate_ips(cidr)`**
  Converts CIDR notation into a list of IP addresses.

* **`find_live_hosts(ips)`**
  Uses Nmap ping scan (`-sn`) to identify active hosts.

* **`scan_ports(live_ips)`**
  Performs port scanning on common ports.

* **`save_json(results)`**
  Stores scan results in JSON format.

* **`generate_markdown(results, subnet)`**
  Creates a structured Markdown report.

---

## 🐳 Docker Usage

### 🔹 Build Docker Image

```bash
docker build -t subnet-scanner .
```

---

### 🔹 Run Container

```bash
docker run -it subnet-scanner
```

Enter CIDR input when prompted.

⚠️ Note: Port results inside Docker may differ due to container networking.

---

## 📌 Notes

* Requires Nmap installed and configured
* Uses common ports for faster scanning
* Output files are generated automatically after execution
* Docker ensures consistent environment setup

---

## 🎥 Demonstration

A video demonstration showcasing:

* Script execution
* Output generation
* Docker usage

is included as part of the submission.

---

## 👨‍💻 Author

**Aaditya Tripathi**

---

## ⭐ Conclusion

This project demonstrates practical knowledge of:

* Network scanning
* Python scripting
* Tool integration (Nmap)
* Output formatting
* Containerization with Docker

It is designed to be simple, extensible, and production-ready.
