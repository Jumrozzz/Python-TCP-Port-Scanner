# PyScanner: Multithreaded Network Port Scanner 🛡️

PyScanner is a fast, efficient, and lightweight Python tool designed to scan a target IP address for common open ports. This tool is built for cybersecurity enthusiasts and ethical hackers to assist in the initial phases of network reconnaissance.



## ✨ Key Features
* **High Performance:** Uses multithreading (15 threads) to scan ports rapidly.
* **Service Identification:** Automatically identifies common services like HTTP, FTP, SSH, and RDP.
* **Clean Output:** Displays results in an organized, color-coded table.
* **Robust Error Handling:** Designed to skip unresponsive ports without crashing the script.

## 🚀 Getting Started

### Prerequisites
* Python 3.x installed on your system.
* Standard Python libraries (`socket`, `threading`, `queue`).

### Installation
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/PyScanner.git]
   cd PyScanner
Run the tool:

Bash
python port_scanner.py
Usage:
When prompted, enter the target IP address (e.g., 127.0.0.1 or a local network IP like 192.168.1.1).

🛠️ How it Works
The scanner attempts to establish a TCP connection with the target. If the connection is successful, the port is marked as OPEN.

Green: Indicates an active, open port.

Red: Indicates the port is closed or unreachable.

⚠️ Ethical Use Disclaimer
This tool is for educational and authorized security testing purposes only. Scanning networks or devices without explicit permission is illegal and unethical. Use this tool responsibly.

Maintained by: Jumroz
