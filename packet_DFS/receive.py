# !/usr/bin/python

import sys
import time
from scapy.all import *
from hdrs import *
from decode import *
from upload import *
from decode_v1 import *
from upload_v1 import *
from upload_end2end import *
from upload_num import *


def main():
    if len(sys.argv) != 2:
        print("Expect VTEP-pair as argument!")
        sys.exit(1)
    paths = [sys.argv[1]]

    # packets sniff
    pkts = sniff(iface="eth0", count=10)
    print("Receiving... ")

    # 1. VXLAN-basd INT (v1)
    meta = []
    DecodeV1(meta, pkts, paths)
    UploadV1(meta, paths)

    # 2. DFS-basd INT
    Decode(int_dict, pkts, paths)
    Upload(int_dict, paths)

    # 3. end-to-end delay
    meta = []
    DecodeV1(meta, pkts, paths)
    Uploadend2end(meta, paths)

    # # 4. packet loss rate
    # pkts = sniff(iface="eth0", timeout=60)
    # print("Receiving... ")
    # Decode(int_dict, pkts, paths)
    # Upload_num(int_dict, paths)


if __name__ == '__main__':
    main()
