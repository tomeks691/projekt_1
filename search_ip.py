from icmplib import ping
import os
import netifaces
from netaddr import IPAddress


def get_amount_hosts():
    subnet_mask = netifaces.ifaddresses("eth0")[netifaces.AF_INET][0]['netmask']
    cidr_subnet = sum(bin(int(x)).count('1') for x in subnet_mask.split('.'))
    return 2 ** (32 - cidr_subnet) - 2

starting_ip = os.popen("hostname -I").read().strip()
starting_ip = starting_ip[:starting_ip.rindex(".")+1]
hosts = get_amount_hosts()
for end_ip in range(0, hosts+1):
    ip = starting_ip + str(end_ip)
    host = ping(ip, count=1)
    print(ip)
    if host.packets_received == 1:
        with open("ips.txt", "a", encoding="UTF-8") as f:
            f.write(f"{ip} \n")