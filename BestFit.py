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

def bestFit(blockSize, m, processSize, n):
    allocation = [-1] * n

    for i in range(n):
        bestIdx = -1
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                if bestIdx == -1:
                    bestIdx = j
                elif blockSize[bestIdx] > blockSize[j]:
                    bestIdx = j

        if bestIdx != -1:
            allocation[i] = bestIdx
            blockSize[bestIdx] -= processSize[i]

    print("Process No. Process Size	 Block no.")
    for i in range(n):
        print(i + 1, "		 ", processSize[i], end="		 ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")

# Driver code
if __name__ == '__main__':
    blockSize, m, processSize, n = takeInputs()
    bestFit(blockSize, m, processSize, n)
