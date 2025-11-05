import re

text = """
Hello, check my website: https://example.com or http://test.org.
My IP address is 192.168.1.10 and another server is 10.0.0.5.
My PAN number is ABCDE1234F. 
Important dates: 12/05/2023, 2022-10-15, and 05-11-24.
"""

print("\n===== ORIGINAL TEXT =====\n")
print(text)

# -------------------------------
# REGEX PATTERNS
# -------------------------------

# URL
url_pattern = r"https?://[^\s]+"

# IPv4 Address
ip_pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"

# Date (dd/mm/yyyy OR yyyy-mm-dd OR dd-mm-yy)
date_pattern = r"\b(?:\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{4}-\d{2}-\d{2})\b"

# PAN Number (ABCDE1234F)
pan_pattern = r"\b[A-Z]{5}[0-9]{4}[A-Z]\b"


# -------------------------------
# FIND ALL MATCHES
# -------------------------------
urls = re.findall(url_pattern, text)
ips = re.findall(ip_pattern, text)
dates = re.findall(date_pattern, text)
pans = re.findall(pan_pattern, text)


# -------------------------------
# OUTPUT
# -------------------------------
print("\n===== URLs FOUND =====")
print(urls)

print("\n===== IP ADDRESSES FOUND =====")
print(ips)

print("\n===== DATES FOUND =====")
print(dates)

print("\n===== PAN NUMBERS FOUND =====")
print(pans)
