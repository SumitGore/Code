def getMaxRequests(serverCapacity, incomingRequests, k):
    n = len(serverCapacity)
    gains = []
    normal_handled = []
    
    # Step 1: Calculate gains for each server
    for i in range(n):
        normal = min(serverCapacity[i], incomingRequests[i])
        doubled = min(serverCapacity[i] * 2, incomingRequests[i])
        gain = doubled - normal
        gains.append((gain, i))
        normal_handled.append(normal)
    
    # Step 2: Pick k largest gains
    gains.sort(reverse=True)
    doubled_indices = set()
    for idx in range(k):
        if idx < n:  # Make sure k is not greater than number of servers
            doubled_indices.add(gains[idx][1])
    
    # Step 3: Compute total
    total = 0
    for i in range(n):
        if i in doubled_indices:
            total += min(serverCapacity[i]*2, incomingRequests[i])
        else:
            total += min(serverCapacity[i], incomingRequests[i])
    
    return total

if __name__ == "__main__":
    # Step 1: Get number of servers
    server_count = int(input("Enter the number of servers: "))

    # Step 2: Get capacities
    print(f"Enter the capacity of each server (space separated):")
    serverCapacity = list(map(int, input().strip().split()))
    if len(serverCapacity) != server_count:
        print("Number of capacities does not match number of servers!")
        exit()

    # Step 3: Get incoming requests
    print(f"Enter the incoming requests for each server (space separated):")
    incomingRequests = list(map(int, input().strip().split()))
    if len(incomingRequests) != server_count:
        print("Number of incoming requests does not match number of servers!")
        exit()

    # Step 4: Get value of k
    k = int(input("Enter the value of k: "))

    # Step 5: Get the result
    result = getMaxRequests(serverCapacity, incomingRequests, k)
    print("Maximum requests handled:", result)
