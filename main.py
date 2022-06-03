import ipaddress
from ssh import client


if __name__ == "__main__":
    ips = [str(ip) for ip in ipaddress.IPv4Network('192.168.127.254/20', False)]
    for ip in ips:
        ip_up = f'ip firewall mangle add chain=prerouting action=mark-packet new-packet-mark={ip}_up passthrough=no src-address={ip} log=no log-prefix=""'
        ip_down = f'ip firewall mangle add chain=prerouting action=mark-packet new-packet-mark={ip}_down passthrough=no dst-address={ip} log=no log-prefix=""'
        print(ip_up)
        print(ip_down)
        client.exec_command(ip_up)
        client.exec_command(ip_down)