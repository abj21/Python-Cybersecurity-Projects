# DAY05 - Subdomain Finder

## Overview

The Subdomain Finder is a Python-based reconnaissance tool that helps discover common subdomains associated with a target domain. It works by testing a predefined list of subdomains and checking whether they respond to HTTP requests.

This project is part of my **20-Day Python Cybersecurity Project Series** and focuses on basic reconnaissance and information gathering techniques used in cybersecurity.

## Features

* Finds common subdomains of a target domain
* Uses HTTP requests to check subdomain availability
* Beginner-friendly implementation
* Demonstrates basic reconnaissance concepts
* Simple and lightweight

## Technologies Used

* Python 3
* Requests Library

## Project Structure

DAY05_Subdomain_Finder/
│
├── sub_domain.py
├── README.md
└── screenshot.png

## How It Works

The program:

1. Accepts a target domain from the user.
2. Appends common subdomains from a predefined wordlist.
3. Sends HTTP requests to each generated URL.
4. Displays discovered subdomains that respond successfully.

Example:

Target Domain:

google.com

Generated URLs:

[www.google.com](http://www.google.com)
mail.google.com
ftp.google.com
blog.google.com
api.google.com

## Installation

Install the required dependency:

pip install requests

## Usage

Run the script:

python3 sub_domain.py

Enter the target domain when prompted:

Enter target domain: google.com

## Example Output

Scanning...

[+] Found: http://www.google.com
[+] Found: http://mail.google.com

Scan Completed

## Cybersecurity Concepts Learned

* Reconnaissance
* Subdomain Enumeration
* Information Gathering
* HTTP Requests
* Exception Handling
* Basic Automation

## Learning Outcome

Through this project, I learned how security professionals perform subdomain enumeration during the reconnaissance phase of penetration testing and how Python can automate information gathering tasks.

## Disclaimer

This project is created for educational purposes only. Use it only on systems and domains that you own or have permission to test.
