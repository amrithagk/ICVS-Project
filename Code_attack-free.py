#Transfer CAN bus packets from vcan0 to vcan1

from scapy.all import *
import threading
import time

load_contrib("cansocket")
load_layer("can")

socket0 = CANSocket(channel="vcan0")
socket1 = CANSocket(channel="vcan1")

def forward(pkt):
    return pkt

def bridge():
    while True:
        bsocket0 = CANSocket(channel="vcan0")
        bsocket1 = CANSocket(channel="vcan1")
        bridge_and_sniff(if1=bsocket0, if2=bsocket1, xfrm12=forward, xfrm21=forward, timeout=1)
        bsocket0.close()
        bsocket1.close()

threadBridge = threading.Thread(target=bridge)
threadBridge.start()

socket0.close()
socket1.close()
