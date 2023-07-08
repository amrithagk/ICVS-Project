# ICVS Project
## Demonstrating the vulnerability in the CAN bus by intercepting packets from the incoming channel and forwarding modified data to the receiving channel.

### The simulation is performed using the virtual instrument cluster simulator, __ICSim__.
### To set up 2 channels
    sudo ip link add dev vcan0 type vcan
    sudo ip link set up vcan0
    sudo ip link add dev vcan1 type vcan
    sudo ip link set up vcan1

## To run the files
#### Terminal 1  
##### &emsp; Attack-free scenario  
&emsp;&emsp;   `python3 "Code_Free flow.py"`   
#####  &emsp; Attack scenario  
&emsp;&emsp;    `python3 Code_MitM.py`  

#### Terminal 2 (For the controller)  
 &emsp;&emsp;   `./controls vcan0`  
####  Terminal 3 (For the simulator)  
&emsp;&emsp;    `./icsim vcan1`  
####  Terminal 4 (To view the packets on the sending side)  
 &emsp;&emsp;   `candump vcan0`  
####  Terminal 5 (To view the packets on the receiving side)  
 &emsp;&emsp;   `candump vcan1 -a`  

