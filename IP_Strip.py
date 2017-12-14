import socket
import re

valid = set()

with open('input.txt') as f_input:
    for ip in re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', f_input.read()):
        try:
            socket.inet_aton(ip)
            valid.add(ip)
        except socket.error:
            pass

print list(valid)ip
