\# CyberKnight CIDR Subnet Scanner



\## 📌 Description



This project is a Python-based network scanner that takes a CIDR subnet as input, identifies live hosts, performs port scanning, and generates outputs in JSON and Markdown formats.



\---



\## 🚀 Features



\* CIDR subnet scanning

\* Live host detection using Nmap

\* Port scanning of active hosts

\* JSON output for machine-readable data

\* Markdown report for human-readable analysis



\---



\## 🛠️ Technologies Used



\* Python

\* Nmap

\* python-nmap

\* netaddr



\---



\## 📦 Installation



\### 1. Clone the repository



```bash

git clone https://github.com/aaditripi18/cyberknight-subnet-scanner.git

cd cyberknight-subnet-scanner

```



\### 2. Install dependencies



```bash

pip install -r requirements.txt

```



\### 3. Install Nmap



Download and install from: https://nmap.org/download.html



\---



\## ▶️ Usage



Run the script:



```bash

python scanner.py

```



Enter a CIDR subnet:



```bash

192.168.1.0/24

```



\---



\## 📄 Output



\### JSON Output (`output.json`)



```json

{

&#x20; "127.0.0.1": \[445]

}

```



\### Markdown Report (`report.md`)



Contains:



\* Scan time

\* Subnet

\* Live IPs

\* Open ports



\---



\## 🎥 Demonstration



A video demonstration of the script execution is included as part of the submission.



\---



\## 📌 Notes



\* Requires Nmap to be installed and available in system PATH

\* Port scan uses common ports for faster execution



\---



\## 👨‍💻 Author



Aaditya Tripathi



