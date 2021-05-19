#!/usr/bin/env python3
from sys import argv
import requests
import re

if len(argv) != 4:
    print("Usage: %s ip port flag" % (argv[0]))
    exit(1)

ip = argv[1]
port = argv[2]
flag = argv[3]

url = "http://%s:%s" % (ip, port)

real_flag = requests.get(url+"/flag").text.strip()

if real_flag==flag:
    print("Pass!")
else:
    print(f"{real_flag} != {flag}")