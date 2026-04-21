# Port Scanner (Task-3)

## Objective

The objective of this task is to develop a simple Python-based port scanner that checks whether commonly used network ports on a target system are open or closed.

## Description

This project is a basic port scanning tool created using Python's socket module. The program scans selected common ports on a user-provided IP address and determines whether those ports are open or closed.

Port scanning is an important technique in cybersecurity that helps identify active services running on a system.

The scanner checks the following common ports:

* Port 80 (HTTP)
* Port 443 (HTTPS)
* Port 445 (SMB)
* Port 3389 (Remote Desktop Protocol)

## Tools & Technologies Used

* Python
* Socket Module
* VS Code

## How It Works

1. The program asks the user to enter a target IP address.
2. It scans selected common ports one by one.
3. It attempts to connect to each port.
4. If the connection is successful:

   * The port is OPEN
5. If the connection fails:

   * The port is CLOSED
6. The results are displayed in the terminal.

## Example Output

Enter target IP address: 127.0.0.1

Scanning target 127.0.0.1...

Port 80 is CLOSED
Port 443 is CLOSED
Port 445 is OPEN
Port 3389 is CLOSED

Scanning completed.

## Learning Outcome

Through this task, I learned:

* Basics of port scanning techniques
* How network services run on different ports
* Using Python socket module for network communication
* Identifying open and closed ports on a system

## Conclusion

This project demonstrates how Python can be used to perform basic port scanning on a target machine. It provides foundational knowledge about network service detection and strengthens understanding of cybersecurity scanning techniques.
