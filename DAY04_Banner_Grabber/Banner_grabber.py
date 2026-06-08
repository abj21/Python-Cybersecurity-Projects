import socket

def banner_grab(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)

        result = s.connect_ex((target, port))

        if result == 0:
            print(f"\n[+] Port {port} is Open")

            try:
                banner = s.recv(1024).decode().strip()
                print(f"[+] Banner: {banner}")
            except:
                print("[!] No banner received")

        s.close()

    except Exception as e:
        print(f"Error: {e}")


target = input("Enter target IP or domain: ")

common_ports = [21, 22, 25, 80, 110, 143, 443]

print(f"\nScanning {target}...\n")

for port in common_ports:
    banner_grab(target, port)