import socket
import threading
from queue import Queue
import time

GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"
BOLD = "\033[1m"

COMMON_PORTS = {
    21: "FTP", 22: "SSH", 23: "TELNET", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 111: "RPCBIND", 135: "MSRPC", 
    139: "NETBIOS", 143: "IMAP", 443: "HTTPS", 445: "MICROSOFT-DS",
    993: "IMAPS", 995: "POP3S", 1723: "PPTP", 3306: "MYSQL", 
    3389: "RDP", 5900: "VNC", 8080: "HTTP-PROXY"
}

def scan_port(target, port, results):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        result = s.connect_ex((target, port))
        
        service = COMMON_PORTS.get(port, "Unknown")
        
        if result == 0:
            results.append((port, "OPEN", service))
        else:
            results.append((port, "CLOSED", service))
            
        s.close()
    except Exception:
        pass

def thread_worker(target, queue, results):
    while not queue.empty():
        port = queue.get()
        scan_port(target, port, results)
        queue.task_done()

def main():
    # Aapka bheja hua ASCII Art yahan add kar diya hai
    print(f"""{BLUE}{BOLD}
  _____   ____  _____ _______    _____  _____          _   _ 
 |  __ \ / __ \|  __ \__   __|  / ____|/ ____|   /\   | \ | |
 | |__) | |  | | |__) | | |    | (___ | |       /  \  |  \| |
 |  ___/| |  | |  _  /  | |     \___ \| |      / /\ \ | . ` |
 | |    | |__| | | \ \  | |     ____) | |____ / ____ \| |\  |
 |_|     \____/|_|  \_\ |_|    |_____/ \_____/_/    \_\_| \_|
    {RESET}""")
    
    print(f"{BLUE}{BOLD}=== Perfectly Aligned PyScanner ==={RESET}\n")
    target = input("Enter Target IP: ").strip()
    
    if not target: return

    port_queue = Queue()
    scan_results = []
    
    for port in sorted(COMMON_PORTS.keys()):
        port_queue.put(port)

    for _ in range(15):
        t = threading.Thread(target=thread_worker, args=(target, port_queue, scan_results))
        t.daemon = True
        t.start()

    port_queue.join()
    
    print(f"\n{BOLD}{'PORT':<10} {'STATUS':<15} {'SERVICE':<15}{RESET}")
    print("-" * 40)

    for port, status, service in sorted(scan_results):
        color = GREEN if status == "OPEN" else RED
        
        print(f"{port:<10} {color}{status:<15}{RESET} {service:<15}")

    print(f"\n{BLUE}Scan Complete.{RESET}")

if __name__ == "__main__":
    main()