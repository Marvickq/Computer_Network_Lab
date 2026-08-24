import math


# ------------------------------------------------------------
# Convert IP address to 32-bit integer
# ------------------------------------------------------------
def ip_to_int(ip):
    parts = ip.split(".")
    result = 0

    for part in parts:
        result = (result << 8) | int(part)

    return result


# ------------------------------------------------------------
# Convert 32-bit integer to IP address
# ------------------------------------------------------------
def int_to_ip(ip):
    return (
        str((ip >> 24) & 255) + "." +
        str((ip >> 16) & 255) + "." +
        str((ip >> 8) & 255) + "." +
        str(ip & 255)
    )


# ------------------------------------------------------------
# Determine IP Class
# ------------------------------------------------------------
def get_class(first_octet):

    if 1 <= first_octet <= 126:
        return "A"

    elif 128 <= first_octet <= 191:
        return "B"

    elif 192 <= first_octet <= 223:
        return "C"

    elif 224 <= first_octet <= 239:
        return "D"

    else:
        return "E"


# ------------------------------------------------------------
# Get Default Prefix
# ------------------------------------------------------------
def get_default_prefix(ip_class):

    if ip_class == "A":
        return 8

    elif ip_class == "B":
        return 16

    elif ip_class == "C":
        return 24

    else:
        return 0


# ------------------------------------------------------------
# Convert Prefix to Subnet Mask
# ------------------------------------------------------------
def prefix_to_mask(prefix):

    if prefix == 0:
        return 0

    return (0xFFFFFFFF << (32 - prefix)) & 0xFFFFFFFF


# ------------------------------------------------------------
# SUBNETTING FUNCTION
# ------------------------------------------------------------
def subnetting(ip, required_subnets):

    # Convert IP to integer
    ip_int = ip_to_int(ip)

    # Find first octet
    first_octet = (ip_int >> 24) & 255

    # Find IP class
    ip_class = get_class(first_octet)

    # Class D and E cannot be used for normal subnetting
    if ip_class == "D" or ip_class == "E":

        print("\nClass", ip_class,
              "does not support normal subnetting.")

        return

    # Get default prefix
    default_prefix = get_default_prefix(ip_class)

    # --------------------------------------------------------
    # Find number of bits to borrow
    # --------------------------------------------------------

    borrowed_bits = 0

    while (2 ** borrowed_bits) < required_subnets:
        borrowed_bits += 1

    # New prefix
    new_prefix = default_prefix + borrowed_bits

    # Maximum practical subnetting for this program
    if new_prefix > 30:

        print("\nToo many subnets requested for this IP class.")

        return

    # --------------------------------------------------------
    # Calculate masks
    # --------------------------------------------------------

    default_mask = prefix_to_mask(default_prefix)
    new_mask = prefix_to_mask(new_prefix)

    # --------------------------------------------------------
    # Number of actual subnets
    # --------------------------------------------------------

    total_subnets = 2 ** borrowed_bits

    # --------------------------------------------------------
    # Hosts per subnet
    # --------------------------------------------------------

    host_bits = 32 - new_prefix

    hosts_per_subnet = (2 ** host_bits) - 2

    # Total usable hosts
    total_hosts = total_subnets * hosts_per_subnet

    # --------------------------------------------------------
    # Calculate network address
    # --------------------------------------------------------

    network_address = ip_int & default_mask

    # --------------------------------------------------------
    # Calculate entire network range
    # --------------------------------------------------------

    first_ip = network_address

    last_ip = network_address + (2 ** (32 - default_prefix)) - 1

    # --------------------------------------------------------
    # OUTPUT
    # --------------------------------------------------------

    print("\nIP Address :", ip)

    print("IP Class   : Class", ip_class)

    print(
        "Default Subnet :",
        int_to_ip(default_mask),
        "/" + str(default_prefix)
    )

    print(
        "New Subnet Mask :",
        int_to_ip(new_mask),
        "/" + str(new_prefix)
    )

    print("Bits Borrowed :", borrowed_bits)

    # --------------------------------------------------------
    # IP ADDRESS RANGE
    # --------------------------------------------------------

    print("\n--------------------------------------------")
    print("IP ADDRESS RANGE")
    print("--------------------------------------------")

    print("Network Address :", int_to_ip(first_ip))

    print("First IP        :", int_to_ip(first_ip + 1))

    print("Last IP         :", int_to_ip(last_ip - 1))

    print("Broadcast Address:", int_to_ip(last_ip))

    # --------------------------------------------------------
    # SUBNET INFORMATION
    # --------------------------------------------------------

    print("\n--------------------------------------------")
    print("SUBNET INFORMATION")
    print("--------------------------------------------")

    print("Required Subnets :", required_subnets)

    print("Actual Subnets   :", total_subnets)

    print("Hosts per Subnet :", hosts_per_subnet)

    print("Total Usable Hosts:", total_hosts)

    # --------------------------------------------------------
    # LIST ALL SUBNETS
    # --------------------------------------------------------

    print("\n--------------------------------------------")
    print("LIST OF ALL SUBNETS")
    print("--------------------------------------------")

    subnet_size = 2 ** host_bits

    print(
        f"{'Subnet':<10}"
        f"{'Network':<18}"
        f"{'First Host':<18}"
        f"{'Last Host':<18}"
        f"{'Broadcast':<18}"
    )

    print("-" * 82)

    for i in range(total_subnets):

        # Network address of subnet
        subnet_network = network_address + (i * subnet_size)

        # Broadcast address
        subnet_broadcast = subnet_network + subnet_size - 1

        # First host
        first_host = subnet_network + 1

        # Last host
        last_host = subnet_broadcast - 1

        print(
            f"{i + 1:<10}"
            f"{int_to_ip(subnet_network):<18}"
            f"{int_to_ip(first_host):<18}"
            f"{int_to_ip(last_host):<18}"
            f"{int_to_ip(subnet_broadcast):<18}"
        )


# ------------------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------------------

ip = input("Enter IP Address: ")

required_subnets = int(
    input("Enter required number of subnets: ")
)

if required_subnets <= 0:

    print("Error: Number of subnets must be greater than 0.")

else:

    subnetting(ip, required_subnets)