#Scapy crafting and analyzing network packets
#Creating a ping packet
from scapy.all import IP, ICMP, sr1
#Create an ICMP packet
packet = IP(dst="192.168.1.1") / ICMP()
#Send the packet and recieve a response
response = sr1(packet)
#print response
print(response)

