#!/usr/bin/env python3
import sys
import json
import urllib.request
import socket
import time

for line in sys.stdin:
    ip = line.strip()
    if not ip:
        continue
    try:
        url = f"https://ipinfo.io/{ip}/json"
        with urllib.request.urlopen(url) as r:
            data = json.loads(r.read())
        org      = data.get("org", "n/d")
        city     = data.get("city", "n/d")
        country  = data.get("country", "n/d")
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            hostname = "n/d"
        print(f"{ip:20s}  {country}  {city:20s}  {hostname:40s}  {org}")
    except Exception as e:
        print(f"{ip:20s}  ERRORE: {e}")
    time.sleep(0.3)
