import requests
import json
server_ips = []
with open("ips.txt") as f:
    for ip in f.readlines():
        server_ips.append(ip.rstrip())
for ip in server_ips:
    response = requests.get(f"http://{ip}")
    with open(f"headers_{ip}.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(dict(response.headers), indent=4))