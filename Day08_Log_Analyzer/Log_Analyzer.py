from collections import Counter

file = open("sample.log", "r")

ips = []

for line in file:
    ip = line.split()[0]  # first word = IP
    ips.append(ip)

file.close()

count = Counter(ips)

print("Total Requests:", len(ips))
print("Unique IPs:", len(count))

print("\nTop IPs:")

for ip, num in count.items():
    print(ip, "->", num)