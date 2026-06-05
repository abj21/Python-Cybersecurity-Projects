import socket
import threading
import time

target = input("Enter IP Address or Domain: ")

start_port = int(input("Enter Start Port: "))
end_port = int(input("Enter End Port: "))

print("Scanning", target)
print("-------------------")

start_time = time.time()

def scan(port):

    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    scanner.settimeout(1)

    result = scanner.connect_ex((target, port))

    if result == 0:
        print("Port", port, "is OPEN")

    scanner.close()

threads = []

for port in range(start_port, end_port + 1):

    thread = threading.Thread(target=scan, args=(port,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end_time = time.time()

print("Scan Completed!")
print("Time Taken:", round(end_time - start_time, 2), "seconds")