# !/usr/bin/python

import sys
from scapy.all import *
from hdrs import *
from decode import *
from upload_num import *


def main():
    if len(sys.argv) != 2:
        print("Expect VTEP-pair as argument!")
        sys.exit(1)
    paths = [sys.argv[1]]

    # packets sniff
    # pkts = sniff(iface="eth0", count=20)
    pkts = sniff(iface="eth0", timeout=30)
    print("Receiving... ")

    Decode(int_dict, pkts, paths)
    Upload_num(int_dict, paths)


if __name__ == '__main__':
    main()
