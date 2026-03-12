Multi-Threaded Network Port Scanner
A high-performance Python utility designed to identify open TCP ports on a target host. This project demonstrates the practical application of Socket Programming and Concurrency in network security.

Features:
Fast Execution: Implements ThreadPoolExecutor to perform concurrent scans, significantly reducing the time required to check 1,024+ ports.

TCP Handshake Logic: Utilizes the full TCP three-way handshake to accurately determine port status.

Dynamic Input: Features a Command Line Interface (CLI) for targeting specific IP addresses or hostnames.

Error Handling: Robust exception management for network timeouts and unreachable hosts.

Technical Stack : 
Language: Python 3.x

Libraries: socket (Network communication), concurrent.futures (Multi-threading)

How to Run:
Clone the repository:

Bash
git clone https://github.com/YOUR_USERNAME/tools-and-scripts.git
cd tools-and-scripts/network-port-scanner
Execute the script:

Bash
python3 scanner.py
Enter Target: Input the IP address (e.g., 127.0.0.1) or hostname (e.g., scanme.nmap.org) when prompted.

How it Works:
The scanner attempts to establish a connection with the target host on a range of ports. If the connection is successful (Return Code 0), the port is flagged as Open. By using 100+ threads, the scanner avoids waiting for individual timeouts, allowing for rapid network discovery.

Disclaimer:
This tool is intended for educational purposes and authorized security testing only. Unauthorized scanning of networks you do not own or have explicit permission to test is illegal and unethical.
