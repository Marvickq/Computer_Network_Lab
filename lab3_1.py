def subnetting(ip_address, required_subnets):

    # Split IP address
    octets = list(map(int, ip_address.split(".")))

    # Determine default prefix based on IP class
    if octets[0] <= 127:
        default_prefix = 8
    elif octets[0] <= 191:
        default_prefix = 16
    else:
        default_prefix = 24

    # --------------------------------
    # Calculate borrowed bits
    # --------------------------------

    borrowed_bits = 0
    number_of_subnets = 1

    while number_of_subnets < required_subnets:
        borrowed_bits += 1
        number_of_subnets = 2 ** borrowed_bits

    # New prefix
    new_prefix = default_prefix + borrowed_bits

    # Check if prefix is valid
    if new_prefix > 30:
        print("Error: Too many subnets. Not enough host bits.")
        return

    # Host bits remaining
    host_bits = 32 - new_prefix

    # Hosts per subnet
    hosts_per_subnet = (2 ** host_bits) - 2

    # --------------------------------
    # Calculate subnet mask
    # --------------------------------

    mask = [0, 0, 0, 0]

    full_octets = new_prefix // 8
    remaining_bits = new_prefix % 8

    for i in range(full_octets):
        mask[i] = 255

    if remaining_bits > 0:
        mask[full_octets] = 256 - (2 ** (8 - remaining_bits))

    # --------------------------------
    # Find subnetting octet
    # --------------------------------

    if remaining_bits == 0:
        subnet_octet = full_octets - 1
    else:
        subnet_octet = full_octets

    block_size = 256 - mask[subnet_octet]

    # --------------------------------
    # Find network address
    # --------------------------------

    network = octets.copy()

    for i in range(subnet_octet + 1, 4):
        network[i] = 0

    network[subnet_octet] = (
        (network[subnet_octet] // block_size) * block_size
    )

    # --------------------------------
    # Display result
    # --------------------------------

    print("\n========== SUBNETTING RESULT ==========")

    print("IP Address        :", ip_address)
    print("Default Prefix    : /", default_prefix)
    print("Required Subnets  :", required_subnets)
    print("Borrowed Bits     :", borrowed_bits)
    print("New Prefix        : /", new_prefix)
    print("Subnet Mask       :", ".".join(map(str, mask)))
    print("Number of Subnets :", number_of_subnets)
    print("Hosts per Subnet  :", hosts_per_subnet)
    print("Block Size        :", block_size)

    # --------------------------------
    # Subnet table
    # --------------------------------

    print("\n========== SUBNET TABLE ==========")

    print(
        f"{'Subnet':<18}"
        f"{'First Host':<18}"
        f"{'Last Host':<18}"
        f"{'Broadcast':<18}"
    )

    print("-" * 72)

    # Convert IP address to integer
    network_int = (
        (network[0] << 24)
        | (network[1] << 16)
        | (network[2] << 8)
        | network[3]
    )

    subnet_size = 2 ** host_bits

    # --------------------------------
    # Convert integer back to IP
    # --------------------------------

    def int_to_ip(value):

        return ".".join([
            str((value >> 24) & 255),
            str((value >> 16) & 255),
            str((value >> 8) & 255),
            str(value & 255)
        ])

    # --------------------------------
    # Generate subnet table
    # --------------------------------

    for subnet_number in range(number_of_subnets):

        subnet_int = network_int + (subnet_number * subnet_size)

        broadcast_int = subnet_int + subnet_size - 1

        first_host_int = subnet_int + 1

        last_host_int = broadcast_int - 1

        subnet_address = int_to_ip(subnet_int)
        first_host = int_to_ip(first_host_int)
        last_host = int_to_ip(last_host_int)
        broadcast = int_to_ip(broadcast_int)

        print(
            f"{subnet_address:<18}"
            f"{first_host:<18}"
            f"{last_host:<18}"
            f"{broadcast:<18}"
        )


# --------------------------------
# MAIN PROGRAM
# --------------------------------

ip = input("Enter IP address: ")

subnets = int(input("Enter required number of subnets: "))

if subnets <= 0:

    print("Error: Number of subnets must be greater than 0.")

else:

    subnetting(ip, subnets)