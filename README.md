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

# 📞 Lab Experiment 4

# Distance Vector Routing

## Aim

To implement the **Distance Vector Routing algorithm** using Python and determine the shortest path and minimum cost between routers in a network.

## Terms

- **Router:** A network device represented by A, B, C, etc.
- **Cost:** The distance/metric required to travel between two routers.
- **Distance Vector:** A table containing the minimum known cost from one router to every destination.
- **Next Hop:** The immediate router through which a packet should be forwarded.
- **INF (999):** Represents no direct connection between two routers.
- **Shortest Path:** The route having the minimum total cost.

## How It Works

1. The user enters the number of routers and the **network cost matrix**.
2. Each router initially knows the cost of reaching itself and its directly connected neighbors.
3. Routers update their distance vectors using the formula:

   ```
   D(i,j) = min(D(i,j), C(i,k) + D(k,j))
   ```
4. The process continues until no routing table changes occur.
5. The final routing tables show the **destination, minimum cost, and next hop**.
6. The user can then enter a source and destination router to find the **shortest path**.

## Student Observation

The Distance Vector algorithm repeatedly exchanges routing information and updates routes when a cheaper path is found. The final routing table contains the minimum cost and next hop for every reachable destination. The experiment demonstrates how routers dynamically determine efficient paths without knowing the complete network topology.

## 📘 Lab 5: TCP Socket Programming

### Aim

To implement client-server communication using Transmission Control Protocol (TCP) in Python.

### Theory

TCP is a connection-oriented transport-layer protocol that provides reliable, ordered delivery of a byte stream. Before exchanging application data, the client establishes a connection with the server.

### Server-Side Procedure

1. Create a TCP socket using Python's `socket` module.
2. Bind the socket to the server's IP address and port number.
3. Call `listen()` to wait for client connections.
4. Use `accept()` to accept an incoming connection.
5. Receive client data using `recv()`.
6. Send a response using `send()` or `sendall()`.
7. Close the connection and release the socket resources.

### Client-Side Procedure

1. Create a TCP socket.
2. Connect to the server using its IP address and port number.
3. Send a message to the server.
4. Receive and display the server's response.
5. Close the connection.

### Important Socket Functions

| Function | Purpose |
|---|---|
| `socket()` | Creates a socket |
| `bind()` | Associates the server socket with a local address |
| `listen()` | Waits for connection requests |
| `accept()` | Accepts a client connection |
| `connect()` | Establishes a client connection |
| `send()` / `sendall()` | Transmits data |
| `recv()` | Receives data |
| `close()` | Closes the socket |

### Result

The TCP client and server establish a connection and exchange messages, demonstrating reliable, connection-oriented communication.

---

## 📘 Lab 6: UDP Socket Programming

### Aim

To implement client-server communication using User Datagram Protocol (UDP) in Python.

### Theory

UDP is a connectionless transport-layer protocol that sends independent datagrams without establishing a connection beforehand. It has lower protocol overhead than TCP but does not guarantee delivery, ordering, or duplicate protection.

### Server-Side Procedure

1. Create a UDP socket using `socket.SOCK_DGRAM`.
2. Bind the socket to a local IP address and port number.
3. Wait for client datagrams using `recvfrom()`.
4. Process the received message.
5. Send a response using `sendto()`.
6. Close the socket when communication is complete.

### Client-Side Procedure

1. Create a UDP socket.
2. Prepare a message for the server.
3. Send the datagram to the server using `sendto()`.
4. Receive the server's response using `recvfrom()`.
5. Display the response and close the socket.

### TCP vs UDP

| Feature | TCP | UDP |
|---|---|---|
| Communication | Connection-oriented | Connectionless |
| Reliability | Reliable delivery | No delivery guarantee |
| Data format | Byte stream | Datagrams |
| Ordering | Ordered byte stream | No ordering guarantee |
| Overhead | Generally higher | Generally lower |
| Examples | Web traffic, file transfer | DNS queries, real-time applications |

### Result

The UDP client and server exchange datagrams without establishing a connection, demonstrating connectionless communication.

---

## 📘 Lab 7: Network Services Configuration Using Cisco Packet Tracer

### Aim

To configure and test DHCP, DNS, Web Server, and Email Server services in Cisco Packet Tracer.

### Objectives

- Assign IP addresses dynamically using DHCP.
- Resolve domain names to IP addresses using DNS.
- Host and access web pages using HTTP.
- Send and receive emails using SMTP and POP3.
- Test connectivity between clients and servers.

### Devices Required

- Cisco Packet Tracer
- PCs or client computers
- Server devices
- Network switch
- Ethernet cables
- Router, if communication across multiple networks is required

### General Network Topology

Connect the PCs and servers to a network switch. Configure each server with an appropriate static IP address. If the topology contains multiple subnets, configure a router and the necessary routes or gateways.

A single server may provide multiple services, or separate servers may be used for DHCP, DNS, web hosting, and email.

### Example IP Addressing Scheme

The following values are illustrative and should be adapted to your actual Packet Tracer topology.

| Device | Example IP Address | Purpose |
|---|---|---|
| Router | `192.168.1.1` | Default gateway |
| DHCP Server | `192.168.1.2` | Automatic IP assignment |
| DNS Server | `192.168.1.3` | Name resolution |
| Web Server | `192.168.1.4` | Website hosting |
| Email Server | `192.168.1.5` | Email services |
| Client PCs | `192.168.1.100` onwards | Access network services |
| Subnet Mask | `255.255.255.0` | Network identification |

Ensure that server IP addresses are excluded from the DHCP address pool to avoid address conflicts.

### 1. Dynamic Host Configuration Protocol (DHCP)

#### Aim

To configure a DHCP server to automatically assign IP addresses and other network parameters to client PCs.

#### Theory

DHCP automatically provides clients with network configuration, including an IP address, subnet mask, default gateway, and DNS server address.

DHCP commonly uses UDP port 67 on the server and UDP port 68 on the client.

#### Configuration Procedure

1. Add a server to the Packet Tracer workspace.
2. Connect the server and client PCs to a switch.
3. Open the server and select **Desktop → IP Configuration**.
4. Assign the server a static IP address, subnet mask, and default gateway.
5. Open **Services → DHCP**.
6. Turn the DHCP service ON.
7. Enter the following settings:
   - Pool Name: `LAN_POOL`
   - Default Gateway: `192.168.1.1`
   - DNS Server: `192.168.1.3`
   - Starting IP Address: `192.168.1.100`
   - Subnet Mask: `255.255.255.0`
   - Maximum Number of Users: `50`
8. Click **Add** to create the pool.
9. Open each client PC and select **Desktop → IP Configuration → DHCP**.
10. Verify that each PC receives a valid IP address and network settings.

#### Verification

- Run `ipconfig` on a client PC to inspect its IP configuration.
- Check that the assigned IP address belongs to the configured DHCP pool.
- Ping the default gateway or another reachable device.

#### Result

The DHCP server dynamically assigns IP addresses and network configuration to client PCs.

### 2. Domain Name System (DNS)

#### Aim

To configure DNS so clients can access servers using domain names rather than numerical IP addresses.

#### Theory

DNS translates domain names into IP addresses. In this experiment, an A record maps a domain name to an IPv4 address.

DNS generally uses UDP port 53 for queries and can also use TCP port 53.

#### Configuration Procedure

1. Add a DNS server or use a server already present in the topology.
2. Assign the server a static IP address, such as `192.168.1.3`.
3. Open **Services → DNS**.
4. Turn the DNS service ON.
5. Add an A record for the website:
   - Name: `www.networklab.local`
   - Address: `192.168.1.4`
6. Click **Add** to save the DNS record.
7. Configure clients to use `192.168.1.3` as their DNS server, either manually or through DHCP.
8. Open a client PC's web browser and enter `http://www.networklab.local`.

#### Example DNS Record

| Field | Value |
|---|---|
| Domain Name | `www.networklab.local` |
| Record Type | A |
| Destination IP | `192.168.1.4` |

The destination IP must match the configured web server address.

#### Verification

- Ping the configured domain name from a client.
- Open the domain name in the web browser.
- Confirm that the website resolves to the correct web server.

#### Result

The DNS server resolves the configured domain name to its corresponding IP address, enabling name-based access to network services.

### 3. Web Server Configuration

#### Aim

To configure a web server and access a hosted web page from client PCs using HTTP.

#### Theory

A web server stores and delivers web content to clients. HTTP is an application-layer protocol commonly used to request and transfer web pages over TCP port 80. HTTPS uses TLS to secure HTTP communication, typically over TCP port 443.

#### Configuration Procedure

1. Add a server and connect it to the network switch.
2. Assign the server a static IP address, such as `192.168.1.4`.
3. Open **Services → HTTP**.
4. Turn HTTP ON.
5. If required, enable HTTPS.
6. Edit the default `index.html` page to display a custom message.
7. Ensure that the DNS server has an A record pointing `www.networklab.local` to `192.168.1.4`.
8. Open a client PC and select **Desktop → Web Browser**.
9. Enter the web server's IP address or domain name.

#### Example

- Web Server IP: `192.168.1.4`
- URL by IP: `http://192.168.1.4`
- URL by domain: `http://www.networklab.local`

#### Verification

- Access the page using the server's IP address.
- Access the same page using the configured domain name.
- Confirm that the custom HTML page loads successfully.

#### Result

The web server hosts and delivers a web page to client PCs over HTTP.

### 4. Email Server Configuration

#### Aim

To configure an email server and exchange messages between client PCs using SMTP and POP3.

#### Theory

An email server enables users to send and retrieve electronic messages.

- **SMTP (Simple Mail Transfer Protocol):** Used to send and relay email.
- **POP3 (Post Office Protocol version 3):** Used by clients to retrieve email from a mailbox.

SMTP commonly uses TCP port 25 in basic lab configurations, while POP3 commonly uses TCP port 110.

#### Server-Side Configuration

1. Add an email server and assign a static IP address, such as `192.168.1.5`.
2. Open **Services → EMAIL**.
3. Set the email domain to `networklab.local`.
4. Enable SMTP and POP3.
5. Create the required user accounts, for example:
   - Username: `alice`, Password: `alice123`
   - Username: `bob`, Password: `bob123`
6. Add each account to the server.

Use these example credentials only in the isolated lab simulation; do not reuse them for real accounts.

#### Client-Side Configuration

1. Open the first client PC.
2. Navigate to **Desktop → Email**.
3. Enter the following details:
   - Display Name: `Alice`
   - Email Address: `alice@networklab.local`
   - Incoming Mail Server: `192.168.1.5`
   - Outgoing Mail Server: `192.168.1.5`
   - Username: `alice`
   - Password: `alice123`
4. Save the configuration.
5. Repeat the process on the second PC for `bob@networklab.local`, using Bob's account credentials.
6. Compose a message from Alice's account addressed to `bob@networklab.local`.
7. Send the email.
8. Open Bob's email application and use the receive/check-mail function.

#### Example Email Configuration

| Parameter | Example |
|---|---|
| Email Domain | `networklab.local` |
| Sender | `alice@networklab.local` |
| Receiver | `bob@networklab.local` |
| Outgoing Protocol | SMTP |
| Incoming Protocol | POP3 |
| Email Server IP | `192.168.1.5` |

#### Verification

- Confirm that SMTP and POP3 are enabled on the server.
- Check that client account credentials and server addresses are correct.
- Send a message from one configured account to another.
- Retrieve the message on the receiving PC and verify its contents.

#### Result

The email server enables message transmission and retrieval between configured email accounts using SMTP and POP3.

---

## 🔍 Network Verification

After configuring the four services, perform these tests:

| Test | Expected Outcome |
|---|---|
| Obtain IP using DHCP | Client receives a valid address from the pool |
| Ping a reachable device | Replies are received if connectivity and policies permit |
| Resolve a DNS name | The name maps to the configured server IP |
| Open the website | The configured HTML page appears |
| Send an email | The sending client submits the message successfully |
| Retrieve an email | The receiving client displays the delivered message |

Use **Simulation Mode** in Cisco Packet Tracer to observe packet exchanges and understand how the protocols operate.

### Troubleshooting Tips

- **DHCP failure:** Check that DHCP is ON, the pool is configured, and the pool has available addresses.
- **DNS failure:** Verify the DNS service, the A record, and the DNS address configured on the client.
- **Website failure:** Confirm that HTTP is ON and the web server IP address is correct.
- **Email failure:** Verify the domain, user accounts, SMTP/POP3 settings, and client credentials.
- **Connectivity failure:** Check cabling, interface status, IP addresses, subnet masks, gateways, and routing where required.

---

## 📚 Protocols Summary

| Protocol | Full Form | Purpose | Transport |
|---|---|---|---|
| DHCP | Dynamic Host Configuration Protocol | Automatic IP configuration | UDP |
| DNS | Domain Name System | Name-to-address resolution | UDP or TCP |
| HTTP | Hypertext Transfer Protocol | Web page transfer | TCP |
| SMTP | Simple Mail Transfer Protocol | Email sending and relay | TCP |
| POP3 | Post Office Protocol v3 | Email retrieval | TCP |
| TCP | Transmission Control Protocol | Reliable, ordered byte-stream communication | Transport protocol |
| UDP | User Datagram Protocol | Connectionless datagram communication | Transport protocol |

## 🎯 Learning Outcomes

After completing these experiments, students should be able to:

- Implement Distance Vector Routing and understand routing-table updates.
- Develop TCP client-server programs using Python sockets.
- Implement UDP communication using datagram sockets.
- Configure DHCP pools and automatically assign IP addresses.


## 🏁 Conclusion

These experiments provide hands-on experience with routing algorithms, socket programming, and application-layer network services. Python is used to explore routing and client-server communication, while Cisco Packet Tracer provides a visual environment for configuring and testing DHCP, DNS, web hosting, and email services.

Together, the experiments strengthen the understanding of computer networks, protocol behavior, client-server architecture, and practical network troubleshooting.
