# 🚀 Lab Experiment 2

## Aim

To implement an **Error Control Protocol** for detecting and controlling errors during data transmission.

## Terms 

### 1. Error Control
**Why needed:** To detect and correct errors that may occur during data transmission.

### 2. Error Detection
**Why needed:** To determine whether the received data contains errors.

### 3. Parity Bit
**Why needed:** To detect simple errors by adding an extra bit to the transmitted data.

### 4. Hamming Code
**Why needed:** To detect and correct single-bit errors in transmitted data.

### 5. Redundancy
**Why needed:** Extra bits are added to the original data to help detect or correct errors.

### 6. Sender
**Why needed:** To transmit the data along with the required error-control information.

### 7. Receiver
**Why needed:** To check the received data for errors and perform correction when possible.

### 8. Error Correction
**Why needed:** To identify and correct an incorrect bit without retransmitting the entire data.

### 9. Retransmission
**Why needed:** To send the data again when an error is detected but cannot be corrected.

# 💡Lab Experiment 3

## Aim

To write a program to demonstrate subnetting and find the subnet mask.

## Terms 

### 1. IP Address
An IP address is a unique address assigned to a device on a network.

**Why needed:**  
It identifies the source and destination devices in a network.

### 2. IPv4 Address
IPv4 is a 32-bit address represented in four octets.

**Why needed:**  
It provides the addressing scheme on which subnetting is performed.

### 3. Subnetting
Subnetting is the process of dividing a larger network into smaller networks called subnets.

**Why needed:**  
It helps divide a network efficiently and manage different groups of devices.

### 4. Subnet
A subnet is a smaller logical network created from a larger network.

**Why needed:**  
It separates devices into smaller network groups and reduces unnecessary network traffic.

### 5. Subnet Mask
A subnet mask determines which portion of an IP address represents the network and which portion represents the host.

**Why needed:**  
It is used to identify the network and determine how the IP address is divided into subnets and hosts.

### 6. Network Address
The network address identifies a particular subnet.

**Why needed:**  
It determines the starting address of a subnet and identifies the network itself.

### 7. Host Address
The host portion identifies an individual device within a subnet.

**Why needed:**  
It allows different devices to be uniquely identified within the same subnet.

### 8. CIDR Notation
CIDR notation represents the number of network bits using a prefix such as `/24`.

**Why needed:**  
It provides a simple way to represent the network portion of an IP address and determine the subnet mask.

### 9. Borrowed Bits
Borrowed bits are host bits taken and used as network bits during subnetting.

**Why needed:**  
They are used to create multiple smaller subnets from one larger network.

### 10. Number of Subnets
The number of subnets is determined using the formula:

`2^n`

where `n` is the number of borrowed bits.

**Why needed:**  
It helps determine how many subnets can be created.

### 11. Number of Hosts
The number of usable hosts in a subnet is determined using:

`2^h - 2`

where `h` is the number of remaining host bits.

**Why needed:**  
It determines how many devices can be assigned IP addresses within each subnet.
