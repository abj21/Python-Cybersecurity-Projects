import socket

ip = input("Enter IP Address: ")

try:
    hostname = socket.gethostbyaddr(ip)
    print("\nHostname:", hostname[0])
except socket.herror:
    print("No hostname found for this IP.")
except Exception as e:
    print("Error:", e)