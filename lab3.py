print("=" * 80)
print("               SUBNETTING AND SUB MASKING PROGRAM")
print("=" * 80)

print("\n1. What is an IP Address?")
print("Answer:")
print("An IP (Internet Protocol) Address is a unique numerical address")
print("assigned to every device connected to a network.")

print("\nExample:")
print("192.168.1.10")
print("=" * 80)

print("\n# DEFINATION: Network Address, Broadcast Address , Usable Hosts, Host Bits ")
print("\nA Host Address is an IP address assigned to an individual device (host) on a network.")
print("\nHost bits:  are the part of an IP address reserved for identifying devices within a network.")
print("Hosts = 2^(Host Bits) - 2")
print("\nNetwork Address   -> First address of the network.")
print("Example           -> 192.168.1.0")
print("Reason            -> All host bits are 0.\n")

print("Broadcast Address -> Last address of the network.")
print("Example           -> 192.168.1.255")
print("Reason            -> All host bits are 1.\n")

print("Usable Hosts      -> Between Network and Broadcast Address.")
print("Example           -> 192.168.1.1 to 192.168.1.254")
print("Reason            -> These addresses can be assigned to devices.")


print("\n" + "-" * 80)

print("2. What is Subnetting?")
print("Answer:")
print("Subnetting is the process of dividing one large network into")
print("multiple smaller logical networks called subnets.")

print("\nWhy is subnetting used?")
print("- Reduces network traffic")
print("- Improves security")
print("- Makes network management easier")
print("- Efficient use of IP addresses")

print("\n" + "-" * 80)

print("3. What is a Subnet Mask?")
print("Answer:")
print("A subnet mask separates the Network ID and Host ID.")

print("\nExample")
print("IP Address  : 192.168.1.25")
print("Subnet Mask : 255.255.255.0")

print("\nNetwork : 192.168.1")
print("Host    : 25")

print("\n" + "-" * 80)

print("4. What is an IP Address Range?")
print("Answer:")
print("The range is the starting and ending IP addresses")
print("belonging to each IP class.")

print("\nClass A : 1.0.0.0 - 126.255.255.255")
print("Class B : 128.0.0.0 - 191.255.255.255")
print("Class C : 192.0.0.0 - 223.255.255.255")
print("Class D : 224.0.0.0 - 239.255.255.255")
print("Class E : 240.0.0.0 - 255.255.255.255")

print("\n" + "-" * 80)

print("5. What is a Loopback Address?")
print("Answer:")
print("Loopback addresses are used to test the local computer.")

print("Range : 127.0.0.0 - 127.255.255.255")
print("Most Common : 127.0.0.1")

print("\n" + "-" * 80)

print("6. Why Number of Hosts = 2^n - 2 ?")

print("Total Addresses = 2^HostBits")
print("-1 Reserved for Network Address")
print("-1 Reserved for Broadcast Address")
print("Usable Hosts = 2^HostBits - 2")

print("\n" + "-" * 80)

print("7. Why can't Class D and Class E be subnetted?")

print("Class D : Used for Multicast Communication.")
print("Class E : Reserved for Experimental purposes.")

print("\n" + "-" * 80)

print("8. Default Subnet Masks")

print("Class A : 255.0.0.0")
print("Class B : 255.255.0.0")
print("Class C : 255.255.255.0")
print("Class D : Not Applicable")
print("Class E : Not Applicable")

print("\n" + "=" * 80)
print("WHY DOES THE PROGRAM PRINT THESE VALUES?")
print("=" * 80)

print("IP Address  -> Shows the user entered IP.")
print("Loopback    -> Checks whether IP is in 127.x.x.x.")
print("Class       -> Identifies the IP Class.")
print("Range       -> Shows valid IP range.")
print("Subnet Mask -> Shows default subnet mask.")
print("Host Bits   -> Used to calculate hosts.")
print("Hosts       -> Calculated using 2^n - 2.")
print("Purpose     -> Shows the purpose of the class.")

print("\n" + "=" * 80)
print("WHY DOES THE TABLE CONTAIN THESE COLUMNS?")
print("=" * 80)

print("Class       -> Identifies the IP Class.")
print("Subnet Mask -> Default subnet mask.")
print("Hosts       -> Maximum usable hosts.")
print("Purpose     -> Main use of the class.")

print("\n" + "=" * 80)
print("HOST CALCULATION")
print("=" * 80)

print("Class A : Host Bits = 24  -> 2^24 - 2 = 16,777,214")
print("Class B : Host Bits = 16  -> 2^16 - 2 = 65,534")
print("Class C : Host Bits = 8   -> 2^8  - 2 = 254")
print("Class D : Not Applicable")
print("Class E : Not Applicable")

print("\n" + "=" * 80)
print("PURPOSE OF EACH CLASS")
print("=" * 80)

print("Class A -> Large Networks")
print("Class B -> Medium Networks")
print("Class C -> Small Networks")
print("Class D -> Multicast")
print("Class E -> Experimental")

print("\n" + "=" * 80)
print("PROGRAM STARTS")
print("=" * 80)

# -------------------------------
# IPv4 Address Classifier
# -------------------------------

import ipaddress

# -------------------------------
# Table of IP Classes
# -------------------------------

classes = {
    "A": {
        "range": "1.0.0.0 - 126.255.255.255",
        "mask": "255.0.0.0",
        "host_bits": 24,
        "purpose": "Large Networks"
    },
    "B": {
        "range": "128.0.0.0 - 191.255.255.255",
        "mask": "255.255.0.0",
        "host_bits": 16,
        "purpose": "Medium Networks"
    },
    "C": {
        "range": "192.0.0.0 - 223.255.255.255",
        "mask": "255.255.255.0",
        "host_bits": 8,
        "purpose": "Small Networks"
    },
    "D": {
        "range": "224.0.0.0 - 239.255.255.255",
        "mask": "Not Applicable",
        "host_bits": 0,
        "purpose": "Multicast"
    },
    "E": {
        "range": "240.0.0.0 - 255.255.255.255",
        "mask": "Not Applicable",
        "host_bits": 0,
        "purpose": "Experimental"
    }
}


# -------------------------------
# Function to Identify Class
# -------------------------------

def identify_class(first_octet):

    if 1 <= first_octet <= 126:
        return "A"

    elif 128 <= first_octet <= 191:
        return "B"

    elif 192 <= first_octet <= 223:
        return "C"

    elif 224 <= first_octet <= 239:
        return "D"

    elif 240 <= first_octet <= 255:
        return "E"

    else:
        return None


# -------------------------------
# Input
# -------------------------------

ip = input("Enter IPv4 Address : ")

# Validate
try:
    address = ipaddress.IPv4Address(ip)

except:
    print("Invalid IPv4 Address")
    exit()

# -------------------------------
# Loopback Check
# -------------------------------

if address.is_loopback:
    print("\nLoopback Address Detected")
    print("Range : 127.0.0.0 - 127.255.255.255")
    print("Purpose : Used to test your own computer.")
    exit()

# -------------------------------
# Class Identification
# -------------------------------

first = int(ip.split(".")[0])

ip_class = identify_class(first)

print("\n---------------------------")
print("IP INFORMATION")
print("---------------------------")

print("IP Address :", ip)
print("Class      :", ip_class)

info = classes[ip_class]

print("Range              :", info["range"])
print("Subnet Mask        :", info["mask"])
print("Purpose            :", info["purpose"])

# -------------------------------
# Hosts
# -------------------------------

if ip_class in ["A", "B", "C"]:

    hosts = (2 ** info["host_bits"]) - 2

    print("Host Bits          :", info["host_bits"])
    print("Hosts per Network  :", hosts)

    print("\nReason")
    print("Total Addresses = 2^HostBits")
    print("Usable Hosts = 2^HostBits - 2")
    print("-1 for Network Address")
    print("-1 for Broadcast Address")

else:

    print("\nNo Hosts Available")
    print("Reason :")
    print("Class D is used for Multicast.")
    print("Class E is reserved for Experimental use.")

# -------------------------------
# Complete Table
# -------------------------------

print("\n==============================================================")
print("{:<8}{:<18}{:<18}{:<15}".format(
    "Class",
    "Subnet Mask",
    "Hosts",
    "Purpose"
))
print("==============================================================")

for c in classes:

    if c in ["A", "B", "C"]:
        h = (2 ** classes[c]["host_bits"]) - 2
    else:
        h = "N/A"

    print("{:<8}{:<18}{:<18}{:<15}".format(
        c,
        classes[c]["mask"],
        str(h),
        classes[c]["purpose"]
    ))

print("==============================================================")

# -------------------------------
# Explanation
# -------------------------------
# Total addresses
total_addresses = 2 ** info["host_bits"]

print("\nAddress Calculation")
print("Total Addresses :", total_addresses)

print("\nReserved Addresses")

print("1. Network Address")
print("Reason : All Host Bits are 0")
print("Example : 192.168.1.0")
print("This address identifies the network itself.")

print("\n2. Broadcast Address")
print("Reason : All Host Bits are 1")
print("Example : 192.168.1.255")
print("This address sends data to every host in the network.")

print("\nUsable Hosts =", total_addresses, "- 2 =", hosts)

print("\nExplanation")
print("-1 Reserved for Network Address")
print("-1 Reserved for Broadcast Address")
print("Therefore Usable Hosts =", hosts)
print("\nWhy -2?")
print("One address is reserved for Network Address.")
print("One address is reserved for Broadcast Address.")
print("Hence usable hosts = 2^n - 2.")

