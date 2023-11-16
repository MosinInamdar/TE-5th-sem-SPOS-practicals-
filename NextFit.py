def takeInputs():
    m = int(input("Enter the number of blocks: "))
    blockSize = []

    for i in range(m):
        blockSize.append(int(input("Enter the size of block {} : ".format(i + 1))))

    n = int(input("Enter the number of processes: "))
    processSize = []

    for i in range(n):
        processSize.append(int(input("Enter the size of process {} : ".format(i + 1))))

    return blockSize, m, processSize, n

def NextFit(blockSize, m, processSize, n):
    allocation = [-1] * n
    j = 0
    t = m-1

    for i in range(n):
        while j < m:
            if blockSize[j] >= processSize[i]:
                allocation[i] = j
                blockSize[j] -= processSize[i]
                t = (j - 1) % m
                break
            if t == j:
                t = (j - 1) % m
                break
            j = (j + 1) % m

    print("Process No. Process Size Block no.")
    
    for i in range(n):
        print("\t", i + 1, "\t\t\t", processSize[i], end="\t\t\t")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")

# Driver Code
if __name__ == '__main__':
    blockSize, m, processSize, n = takeInputs()
    NextFit(blockSize, m, processSize, n)
