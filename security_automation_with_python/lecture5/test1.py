from scapy.all import *

def packet_sniffer():
    print("Starting packet capture...")
    packets = sniff(count=10)  # Capture 10 packets
    packets.show()  # Display captured packets

# Example usage
packet_sniffer()
