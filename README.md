# ICVS Project
### This project demonstrates the modification of CAN Bus packet data by exploiting the vulnerabilities in the CAN Bus network

## The simulation is performed using the ICSim package.

### To set up 2 channels
    sudo ip link add dev vcan0 type vcan
    sudo ip link set up vcan0
    sudo ip link add dev vcan1 type vcan
    sudo ip link set up vcan1

## To run the files
Terminal 1  
Attack-free scenario  
    python3 "Code_Free flow.py"  
Attack scenario  
    python3 Code_MitM.py
Terminal 2 (For the controller)  
    ./controls vcan0  
Terminal 3 (For the simulator)  
    ./icsim vcan1  
Terminal 4 (To view the packets on the sending side)  
    candump vcan0  
Terminal 5 (To view the packets on the receiving side)  
    candump vcan1 -a  

