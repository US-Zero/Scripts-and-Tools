# 🛡️ Multi-Threaded Network Port Scanner

A high-performance Python utility designed to identify open TCP ports on a target host. This project demonstrates the practical application of **Socket Programming** and **Concurrency** in network security.

---

## Features
* **High-Speed Execution:** Implements `ThreadPoolExecutor` to perform concurrent scans, reducing execution time for 1,024 ports by ~80%.
* **TCP Handshake Logic:** Utilizes the full TCP three-way handshake to accurately determine port status.
* **Dynamic CLI:** Features a Command Line Interface for targeting specific IP addresses or hostnames.
* **Error Handling:** Robust exception management for network timeouts and unreachable hosts.

## Technical Stack
* **Language:** Python 3.x
* **Core Modules:** `socket`, `concurrent.futures`, `threading`

## How to Run
1. **Navigate to the directory:**
   ```bash
   cd network-port-scanner
2. **Execute the script:**
    ```bash
    python3 scanner.py
4. **Enter Target :**
    Input the IP (e.g., 127.0.0.1) or hostname (e.g., scanme.nmap.org) when prompted.

## The Logic
* The scanner attempts to establish a connection with the target host. If the connection is successful (Return Code 0), the port is flagged as Open. By using 100 simultaneous threads, the tool avoids the bottleneck of waiting for individual port timeouts.

## Disclaimer
* This tool is intended for educational purposes and authorized security testing only. Unauthorized scanning of networks is illegal and unethical.
