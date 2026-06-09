import requests

domain = input("Enter target domain: ")

subdomains = [
    "www",
    "mail",
    "ftp",
    "blog",
    "dev",
    "test",
    "api",
    "docs",
    "shop"
]

print("\nScanning...\n")

for sub in subdomains:
    url = f"http://{sub}.{domain}"

    try:
        requests.get(url, timeout=2)
        print(f"[+] Found: {url}")
    except requests.ConnectionError:
        pass

print("\nScan Completed")