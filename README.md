# Case-study-replicating-the-Mitnick-Attack-a-TCP-session-hijacking-technique

In this report, we are executing a multi-step attack that exploits trust relationships in networked systems. First, an SYN flooding attack would be initiated to make the trusted server unresponsive, preventing it from resetting a spoofed TCP connection. While the server is withheld, TCP sequence number prediction is performed, analysing patterns in sequence numbers to craft valid packets that appear authentic. With this information, session hijacking and spoofing are executed by forging a connection between the trusted server and the target system. Once access is gained, an rsh command is injected into the hijacked session, modifying the .rhosts file to create a conveniently accessible backdoor. This allows us to maintain unauthorised access in the future without requiring authentication, effectively compromising the system’s security.

Vulnerabilities Exploited
The attack exploits weaknesses in the TCP/IP protocol, particularly the predictability of TCP sequence numbers and the trust relationships between systems.
Experiments


This multi-step attack demonstrates how weaknesses in TCP sequence numbers and trust-based authentication can be exploited:

1. **SYN Flooding** — Silences a trusted host.
2. **Sequence Number Prediction** — Analyzes patterns to forge TCP packets.
3. **Session Hijacking** — Injects spoofed packets into a live session.
4. **Backdoor Implantation** — Adds a trust entry to `.rhosts` for future access.
Key Components of the Attack Scenario 
● Target System: X-Terminal (the system that we want to access)
● Trusted Server: A system with pre-established, password-free access to X-Terminal 

Network Topology 
[Attacker] --- (Spoofed Traffic) ---> [Target System (X-Terminal)] | |--> [Trusted Server (Silenced)]


   
