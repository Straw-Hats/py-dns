#!/usr/bin/env python3

 import argparse
 import dns.zone
 import dns.resolver

 def main(domain):
    # IPv4 DNS Records
    resultV4 = dns.resolver.query(domain, 'A')
    for i in range(0, len(resultV4)):
        print("IPV4 address: ", resultV4[i])

    # IPv6 DNS Records
    try:
        resultV6 = dns.resolver.query(domain, 'AAAA')
        for i in range(0, len(resultV6)):
            print("IPv6: ", resultV6[i])
    except dns.resolver.NoAnswer as e:
        print("Exception in resolving the IPv6 Resource Record:", e)
