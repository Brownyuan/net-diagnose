#!/usr/bin/python

"""
The script validate whether the ip address is in the subsets defined in a file or NOT.
"""

from netaddr import IPNetwork
import sys

ip = sys.argv[1]


def isInSubset(ip, subnet):
    ipInfo = IPNetwork(subnet)
    return ip in ipInfo


def isWhite(ip, filename='./cn.ipset'):
    f = open(filename)
    for net in f:
        if isInSubset(ip, net):
            print "IP {0} is in net {1}".format(ip, net) 
            print "IP {0} is in the white list defined in {1}".format(ip, filename) 
            return True
    print "IP is NOT in the white list defined in {0}".format(filename)
    return False


isWhite(ip)
