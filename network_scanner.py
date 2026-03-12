import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            if s.connect_ex((host, port)) == 0:
                return port
    except:
        return None

def main():
    target = input("Enter target IP or Host (e.g., 127.0.0.1): ")
    print(f"--- Scanning {target} ---")
    
    # Using a ThreadPool to manage 100 simultaneous workers
    with ThreadPoolExecutor(max_workers=100) as executor:
        ports = range(1, 1025)
        results = executor.map(lambda p: scan_port(target, p), ports)
    
    for port in results:
        if port:
            print(f"[+] Port {port} is OPEN")

if __name__ == "__main__":
    main()
