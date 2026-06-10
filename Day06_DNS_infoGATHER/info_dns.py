import dns.resolver

domain = input("Enter domain: ")

record_types = ["A", "AAAA", "MX", "NS", "TXT", "CNAME"]

for record in record_types:
    print(f"\n===== {record} Records =====")

    try:
        answers = dns.resolver.resolve(domain, record)

        for data in answers:
            print(data.to_text())

    except Exception:
        print("No records found")