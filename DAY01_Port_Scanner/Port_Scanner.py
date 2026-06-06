import socket

target = input("Enter IP Address or Domain: ")

print("")
print("Scanning", target)
print("")

for port in range(1, 50):

    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    scanner.settimeout(1)

    result = scanner.connect_ex((target, port))

    if result == 0:
        print("Port", port, "is OPEN")

    scanner.close()

print("")
print("Scan Completed!")
