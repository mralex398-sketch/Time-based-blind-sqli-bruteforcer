# PostgreSQL Time-Based Blind SQL Injection Exploitation Tool (PoC)

This repository contains a specialized Proof of Concept (PoC) script designed to automate the extraction of data via **Time-Based Blind SQL Injection**. The script is tailored for PostgreSQL database environments, specifically targeting challenge architectures found within the PortSwigger Web Security Academy.

---

## 🔬 Vulnerability Analysis & Technical Mechanics

When an application is vulnerable to Blind SQL Injection and does not return any data or errors in the HTTP response, security analysts must rely on time delays to infer the database's internal state. This script automates that exact conditional feedback loop:

1. **Malicious Payload Injection**: The script injects a conditional PostgreSQL query into the target tracking cookie (`TrackingId`):
   ```sql
   '|| CASE WHEN (SELECT COUNT(username) FROM users WHERE username = 'administrator' AND SUBSTRING(Password, 1, 1) = 'a') = 1 THEN pg_sleep(2) ELSE pg_sleep(0) END --
   ```
2. **Boolean Condition via Time Delay**: 
   - If the guessed character at the current string position is **correct**, the database executes `pg_sleep(2)`, forcing the server to delay its response.
   - If the character is **incorrect**, it executes `pg_sleep(0)`, responding instantly.
3. **Delta Time Validation**: The script records precise execution timestamps using Python's `time.time()`. If the round-trip latency exceeds the threshold (\(\ge 1.8\) seconds), the character is confirmed and appended to the password string.
4. **Brute-Force Optimization**: Iterates dynamically through a fixed 20-character position loop against a specific alphanumeric alphabet (`a-z`, `0-9`).

---

## 📋 Requirements & Installation

This automation exploit relies on standard Python 3 execution coupled with the `requests` library.

1. Clone or download this repository into your dedicated project folder:
```bash
git clone https://github.com
cd Time-Based-SQLi-Bruteforcer
```

2. Install the HTTP communication module:
```bash
pip install requests
```

---

## 🚀 Configuration & Execution

> ⚠️ **IMPORTANT LAB CONFIGURATION**: Web Security Academy lab instances regenerate their unique subdomains frequently upon restart. You **must** verify and update the target URL before running the script.

1. Open the script file and update the global `url` variable with your active lab endpoint:
```python
url = "https://<YOUR-ACTIVE-LAB-ID>.web-security-academy.net/"
```

2. Execute the exploit via your terminal:
```bash
python timebasedblindbruteforcer.py
```

### Expected Telemetry:
The tool will print real-time verbose output detailing each matched string index, the specific character recovered, the verified response latency, and the ongoing partial password string until extraction is complete.

---

## ⚖️ Legal & Educational Disclaimer

**IMPORTANT NOTICE:** This tool is developed strictly for educational research, defensive security engineering, and authorized web application penetration testing. 

Running exploitation scripts against unauthorized external targets or corporate web infrastructures without explicit written consent is illegal and punishable by law. The author assumes **no liability** for any misuse, operational impact, or legal consequences arising from the execution of this software.
