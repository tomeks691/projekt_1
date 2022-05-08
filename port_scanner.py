import socket
server_ips = []
with open("ips") as f:
    for ip in f.readlines():
        server_ips.append(ip.rstrip())

for ip in server_ips:
    scanner = socket.gethostbyname(ip)
    with open("open_ports.txt", "a", encoding="utf-8") as f:
        f.write(f"{ip}: ")
    for port in range(1, 1000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"Scanning port: {port}")
        open_ports = sock.connect_ex((ip, port))
        if open_ports == 0:
            with open("open_ports.txt", "a", encoding="UTF-8") as f:
                f.write(f"{port} ")
                sock.close()
    with open("open_ports.txt", "a", encoding="utf-8") as f:
        f.write(f"\n")
