import ipaddress


if __name__ == "__main__":
    ips = [str(ip) for ip in ipaddress.IPv4Network('192.168.127.254/20', False)]
    f = open("ip.txt", "w")
    for ip in ips:
        ip_up = f'ip firewall managle chain=prerouting action=mark-packet new-packet-mark={ip}_up passthrough=no src-address={ip} log=no prefix=""'
        ip_down = f'ip firewall managle chain=prerouting action=mark-packet new-packet-mark={ip}_down passthrough=no dst-address={ip} log=no prefix=""'
        print(ip_up)
        print(ip_down)
        f.write(f"{ip_up}\n")
        f.write(f"{ip_down}\n")
    f.close()