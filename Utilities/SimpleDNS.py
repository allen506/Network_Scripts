#!/usr/bin/python

import socket, os

hostname = input("Enter FQDN:")
limit = int(input("Number of queries:"))

def findips(hostname):
    ipaddr = socket.gethostbyname(hostname)
    print(ipaddr)

for i in range(limit):
    findips(hostname)
