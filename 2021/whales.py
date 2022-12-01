with open("whales.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

npos = [int(pos) for pos in lines[0].split(",")]
npos.sort()
n = len(npos)

totalSum = 0
totalSumOfSquares = 0
sumTillNow = []
sumOfSquaresTillNow = []

for pos in npos:
    sumTillNow.append(totalSum)
    sumOfSquaresTillNow.append(totalSumOfSquares)
    totalSum += pos
    totalSumOfSquares += pos * pos

minDistance = float('inf')
minPos = -1

for i in range(n - 1):
    for curr in range(npos[i], npos[i + 1] + 1):
        # PART 1
        currSum = (2 * i - n) * curr - 2 * sumTillNow[i] + totalSum
        # PART 2
        currNewSum = (n * curr * curr + totalSumOfSquares - 2 * curr * totalSum + currSum) / 2
        # PART 1
        # if currSum < minDistance:
        #     minDistance = currSum
        #     minPos = curr
        # PART 2
        if currNewSum < minDistance:
            minDistance = currNewSum
            minPos = curr

# PART 1
# print(minPos, sum([abs(pos - minPos) for pos in npos]))
# PART 2
print(minPos, sum([abs(pos - minPos) * (abs(pos - minPos) + 1) / 2 for pos in npos]))