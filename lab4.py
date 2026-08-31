INF = 999

# --------------------------------
# INPUT
# --------------------------------

n = int(input("Enter number of routers: "))

print("\nEnter the network cost matrix:")
print(f"Enter {INF} for no direct connection.\n")

cost = []

for i in range(n):

    while True:
        row = list(map(int, input(f"Router {chr(65 + i)}: ").split()))

        if len(row) == n:
            cost.append(row)
            break

        print(f"Please enter exactly {n} values.")


# --------------------------------
# INITIALIZE DISTANCE VECTOR
# --------------------------------

distance = [row[:] for row in cost]

next_hop = [[-1] * n for _ in range(n)]

for i in range(n):

    # Distance from router to itself
    distance[i][i] = 0

    for j in range(n):

        # Directly connected router
        if i != j and cost[i][j] != INF:
            next_hop[i][j] = j


# --------------------------------
# DISTANCE VECTOR ALGORITHM
# --------------------------------

while True:

    changed = False

    # Copy previous routing table
    old_distance = [row[:] for row in distance]
    old_next_hop = [row[:] for row in next_hop]

    for i in range(n):              # Current router

        for k in range(n):          # Neighbor router

            if i == k or cost[i][k] == INF:
                continue

            for j in range(n):      # Destination router

                if old_distance[k][j] == INF:
                    continue

                # Calculate cost through neighbor k
                new_cost = cost[i][k] + old_distance[k][j]

                # Update if shorter path is found
                if new_cost < distance[i][j]:

                    distance[i][j] = new_cost

                    # First hop towards destination
                    next_hop[i][j] = old_next_hop[i][k]

                    changed = True

    # Stop when no routing table changes
    if not changed:
        break


# --------------------------------
# SOURCE AND DESTINATION
# --------------------------------

source_char = input("\nEnter source router: ").upper()
destination_char = input("Enter destination router: ").upper()

source = ord(source_char) - ord('A')
destination = ord(destination_char) - ord('A')


# --------------------------------
# VALIDATE SOURCE AND DESTINATION
# --------------------------------

if not (0 <= source < n) or not (0 <= destination < n):

    print("\nInvalid router entered.")

else:

    # --------------------------------
    # FINAL ROUTING TABLE FROM SOURCE
    # --------------------------------

    print("\n" + "=" * 55)
    print(f"FINAL ROUTING TABLE FROM ROUTER {source_char}")
    print("=" * 55)

    print("Destination\tShortest Distance\tNext Hop")

    for j in range(n):

        destination_name = chr(65 + j)

        # Shortest distance
        if distance[source][j] == INF:
            cost_value = "INF"
        else:
            cost_value = distance[source][j]

        # Next hop
        if next_hop[source][j] == -1:
            hop = "-"
        else:
            hop = chr(65 + next_hop[source][j])

        print(f"{destination_name}\t\t{cost_value}\t\t\t{hop}")


    # --------------------------------
    # SHORTEST PATH
    # --------------------------------

    print("\n" + "=" * 55)
    print("SHORTEST PATH")
    print("=" * 55)

    if distance[source][destination] == INF:

        print(f"No path exists from {source_char} to {destination_char}.")

    else:

        print(f"Source: {source_char}")
        print(f"Destination: {destination_char}")
        print("Minimum Cost:", distance[source][destination])

        # Construct path
        path = [source]
        current = source

        while current != destination:

            current = next_hop[current][destination]

            if current == -1:
                break

            path.append(current)

        # Print path
        print("Path:", end=" ")

        for i in range(len(path)):

            print(chr(65 + path[i]), end="")

            if i != len(path) - 1:
                print(" -> ", end="")

        print()
