

# Take 4 data bits as input
d1, d2, d3, d4 = map(int, input("Enter 4 data bits (D1 D2 D3 D4): ").split())

# Calculate parity bits (Even Parity)
p1 = d1 ^ d2 ^ d4
p2 = d1 ^ d3 ^ d4
p4 = d2 ^ d3 ^ d4

print("\nCalculated Parity Bits:")
print("P1 =", p1)
print("P2 =", p2)
print("P4 =", p4)

# Form Hamming Code
code = [0] * 8      # Ignore index 0

code[1] = p1
code[2] = p2
code[3] = d1
code[4] = p4
code[5] = d2
code[6] = d3
code[7] = d4

print("\nGenerated Hamming Code:", end=" ")
for i in range(1, 8):
    print(code[i], end="")
print()

# Receiver Side
received = list(map(int, input("\nEnter received 7-bit codeword (space separated): ").split()))

# Insert dummy value at index 0 to match positions 1-7
r = [0] + received

# Syndrome Calculation
s1 = r[1] ^ r[3] ^ r[5] ^ r[7]
s2 = r[2] ^ r[3] ^ r[6] ^ r[7]
s4 = r[4] ^ r[5] ^ r[6] ^ r[7]

print("\nSyndrome Bits:")
print("S1 =", s1)
print("S2 =", s2)
print("S4 =", s4)

# Find error position
error = s4 * 4 + s2 * 2 + s1

if error == 0:
    print("\nNo Error Detected.")
else:
    print("\nError Detected at Position:", error)

    # Correct the error
    r[error] = 1 - r[error]

    print("Corrected Codeword:", end=" ")
    for i in range(1, 8):
        print(r[i], end="")
    print()