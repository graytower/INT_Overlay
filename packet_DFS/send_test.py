#!/usr/bin/env python
import sys
from scapy.all import *
from hdrs import *
import time
import MySQLdb


# Send Packet #
def main():
    pkt1 = Ether(src=get_if_hwaddr('eth0'), dst='ff:ff:ff:ff:ff:ff', type=0x0800) / \
           IP(src=get_if_addr('eth0'), dst=sys.argv[1], proto=17) / \
           UDP(dport=4790) / \
           VXLAN(vni=0x100) / \
           PAYLOAD(load=9999)

    # sendp(pkt1, iface='eth0')

    # for i in range(2):
    #     sendp(pkt1, iface='eth0')
    #     time.sleep(0.01)

    # t = time.time()
    # tst = int(round(t * 1000000))

    while True:
        time_now = time.strftime("%H:%M:%S", time.localtime())
        if time_now == "16:04:04":
            print('time!')
            for i in range(500):
                sendp(pkt1, iface='eth0')
                time.sleep(0.001)
            sys.exit()


if __name__ == '__main__':
    main()
