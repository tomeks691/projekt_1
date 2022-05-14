from icmplib import ping
import os

starting_ip = os.popen("hostname -I").read().strip()
starting_ip = starting_ip[:starting_ip.rindex(".")+1]
for end_ip in range(0, 256):
    ip = starting_ip + str(end_ip)
    host = ping(ip, count=1)
    print(ip)
    if host.packets_received == 1:
        with open("ips.txt", "a", encoding="UTF-8") as f:
            f.write(f"{ip} \n")