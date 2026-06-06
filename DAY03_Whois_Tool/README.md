# WHOIS Lookup Tool

## Overview

The WHOIS Lookup Tool is a Python-based reconnaissance tool that retrieves publicly available domain registration information. It helps gather details about a domain such as its registrar, creation date, expiration date, and name servers.

## Features

* Domain WHOIS lookup
* Registrar information
* Creation date retrieval
* Expiration date retrieval
* Updated date retrieval
* Name server information
* Error handling for invalid domains

## Technologies Used

* Python 3
* python-whois library

## Cybersecurity Concept

This project focuses on **Reconnaissance** and **Information Gathering**, which are the first phases of ethical hacking and penetration testing. WHOIS data helps security professionals collect publicly available information about a target domain.

## How It Works

1. User enters a domain name.
2. The script sends a WHOIS request.
3. Domain information is retrieved.
4. Results are displayed in the terminal.

## Usage

Install the required library:

```bash
pip install python-whois
```

Run the program:

```bash
python whois_lookup.py
```

Example:

```text
Enter domain name: google.com

===== WHOIS REPORT =====
Domain Name      : GOOGLE.COM
Registrar        : MarkMonitor Inc.
Creation Date    : 1997-09-15
Expiration Date  : 2028-09-14
```

## Learning Outcomes

* Working with external Python libraries
* Understanding WHOIS records
* Exception handling in Python
* Basic cybersecurity reconnaissance techniques

## Author

Abhinav Jassi

Part of the **20-Day Python Cybersecurity Project Series**.
