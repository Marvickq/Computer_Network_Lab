import ipaddress


def subnetting(network_address, prefix):
    network = ipaddress.ip_network(
        f"{network_address}/{prefix}",
        strict=False
    )

    print("\n========== SUBNETTING ==========")
    print("Network       :", network_address)
    print("Subnet Mask   :", network.netmask)
    print("CIDR          : /", prefix)

    host_bits = 32 - prefix

    # Number of hosts per subnet
    hosts = (2 ** host_bits) - 2

    # Number of subnets relative to /24
    borrowed_bits = prefix - 24

    if borrowed_bits >= 0:
        number_of_subnets = 2 ** borrowed_bits
    else:
        number_of_subnets = 1

    print("Host Bits     :", host_bits)
    print("Hosts/Subnet  :", hosts)
    print("No. of Subnets:", number_of_subnets)

    print("\nSubnet Address | First Host | Last Host | Broadcast")
    print("-" * 65)

    for subnet in network.subnets(new_prefix=prefix):

        first_host = subnet.network_address + 1
        last_host = subnet.broadcast_address - 1

        print(
            f"{str(subnet.network_address):<14} | "
            f"{str(first_host):<11} | "
            f"{str(last_host):<10} | "
            f"{str(subnet.broadcast_address)}"
        )


# Example from Lab 3
subnetting("192.168.10.0", 27)