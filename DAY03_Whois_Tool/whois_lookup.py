import whois

domain = input("Enter domain name: ")

try:
    info = whois.whois(domain)

    print("\n===== WHOIS REPORT =====")
    print("Domain Name      :", info.domain_name)
    print("Registrar        :", info.registrar)
    print("Creation Date    :", info.creation_date)
    print("Expiration Date  :", info.expiration_date)
    print("Updated Date     :", info.updated_date)
    print("Organization     :", info.org)
    print("Country          :", info.country)
    print("Name Servers     :", info.name_servers)

except Exception as e:
    print("Error:", e)
