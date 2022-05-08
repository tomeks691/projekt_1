from icmplib import ping
starting_ip = "192.168.55."
for end_ip in range(0, 256):
    ip = starting_ip + str(end_ip)
    host = ping(ip, count=1, interval=0.2)
    if host.packets_received == 1:
        with open("ips.txt", "a", encoding="UTF-8") as f:
            f.write(f"{ip} \n")