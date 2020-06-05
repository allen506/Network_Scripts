#!/usr/bin/python

import socket, os, dns
import dns.resolver

hostname = input("Enter FQDN:")
limit = int(input("Number of queries:"))
customdns = input("Use A10 as DNS Server?(Y or N): ")
#a10 = '144.77.20.140'
a10 = '8.8.8.8'
defaultdns = '4.2.2.2'
# x = int(limit)

def findips(hostname):
    if customdns.lower() == "y":
        res = dns.resolver.Resolver(configure=False)
        res.nameservers = [a10]
        answer = res.query(hostname, 'a')
        for i in answer:
            print(i)

    elif customdns.lower() == "n":
        res = dns.resolver.Resolver(configure=False)
        res.nameservers = [defaultdns]
        answer = res.query(hostname, 'a')
        for i in answer:
            print(i)
    else:
        print ("Invalid input, try again")

for i in range(limit):
    findips(hostname)
