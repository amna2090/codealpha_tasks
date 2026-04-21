import socket

target = input("Enter target IP address: ")

print(f"\nScanning target {target}...\n")

common_ports = [80, 443, 445, 3389]

for port in common_ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")

    s.close()

print("\nScanning completed.")