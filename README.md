# Network Packet Sniffer (Task-1)

## Objective

The objective of this project is to build a simple network packet sniffer using Python that captures live network traffic and displays important packet details such as source IP address, destination IP address, and protocol type.

## Description

This Python-based packet sniffer captures network packets in real time using the Scapy library. It extracts and prints the source IP address, destination IP address, and protocol type (TCP, UDP, ICMP) for each packet detected on the network.

This tool helps in understanding how network communication works and how packet-level monitoring is performed in cybersecurity.

## Tools & Technologies Used

* Python
* Scapy Library
* VS Code
* Npcap (for Windows packet capturing support)

## How It Works

1. The script starts capturing live network packets.
2. It checks whether the packet contains an IP layer.
3. It extracts:

   * Source IP address
   * Destination IP address
   * Protocol type
4. The protocol number is converted into readable format (TCP / UDP / ICMP).
5. Packet information is displayed in the terminal.

## Example Output

Starting Network Sniffer...

Packet Captured:
Source IP: 192.168.0.103
Destination IP: 142.250.187.46
Protocol: TCP

---

## Learning Outcome

Through this task, I learned:

* Basics of network packet capturing
* Understanding IP packet structure
* Identifying network protocols (TCP, UDP, ICMP)
* Using Scapy for cybersecurity monitoring

## Conclusion

This project demonstrates how Python can be used to capture and analyze network traffic in real time. It is a foundational step toward learning network monitoring and ethical hacking concepts in cybersecurity.
