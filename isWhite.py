#!/usr/bin/python

"""
The script validate whether the ip address is in the subsets defined in a file or NOT.
"""

from netaddr import IPNetwork
import sys
import argparse



def isInSubset(ip, subnet):
    """
        Validate whether ip is in subset
    """
    ipInfo = IPNetwork(subnet)
    return ip in ipInfo


def isWhite(ip, filename='./cn.ipset'):
    """
        Validate whether ip is in the subsets defined in filename
    """
    f = open(filename)
    for net in f:
        if isInSubset(ip, net):
            print "IP {0} is in net {1}".format(ip, net) 
            print "IP {0} is in the white list defined in {1}".format(ip, filename) 
            return True
    print "IP is NOT in the white list defined in {0}".format(filename)
    return False


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('ip', help='ip address to be tested')
    parser.add_argument('--filename', help="file name to be tested against")

    args = parser.parse_args(sys.argv[1:])

    default_filename = './cn.ipset'
    filename = args.filename or default_filename

    isWhite(args.ip, filename)
