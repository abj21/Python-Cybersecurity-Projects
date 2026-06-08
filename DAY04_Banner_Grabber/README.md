# DAY04 - Banner Grabber

## Overview
This project is a simple Python-based Banner Grabber that connects to common network service ports and attempts to retrieve service banners. Banner grabbing is a reconnaissance technique used in cybersecurity to identify running services, software versions, and potential vulnerabilities on a target system.

## Features
- Scans common service ports
- Detects open ports
- Retrieves service banners when available
- Uses Python socket programming
- Includes timeout and error handling

## Technologies Used
- Python 3
- Socket Module

## How It Works
The tool attempts to establish a TCP connection to a target host on common ports such as:

- 21 (FTP)
- 22 (SSH)
- 25 (SMTP)
- 80 (HTTP)
- 110 (POP3)
- 143 (IMAP)
- 443 (HTTPS)

If a service sends a banner upon connection, the tool captures and displays it.
