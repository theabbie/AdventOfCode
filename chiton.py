import heapdict

with open("chiton.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

nodes = {}

n = 5

numRows = len(lines)
numCols = len(lines[0])

def getNeighbors(row, col):
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))
    if row < numRows * n - 1:
        neighbors.append((row + 1, col))
    if col > 0:
        neighbors.append((row, col - 1))
    if col < numCols * n - 1:
        neighbors.append((row, col + 1))
    return neighbors

beg = (0, 0)

nodeHeap = heapdict.heapdict()

nodes[beg] = {
    "dist": 0,
    "visited": False
}

nodeHeap[beg] = 0

def getMinimumNode():
    nodeList = list(nodes)
    minNode = None
    minDist = float("inf")
    for i in nodeList:
        if not nodes[i]["visited"] and nodes[i]["dist"] < minDist:
            minNode = i
            minDist = nodes[i]["dist"]
    return minNode

while len(nodeHeap) > 0:
    i, j = nodeHeap.popitem()[0]
    nodes[(i, j)]["visited"] = True
    val = nodes[(i,j)]["dist"]
    neighbors = getNeighbors(i, j)
    for x, y in neighbors:
        nval = int(lines[x % numRows][y % numCols]) + y // numCols + x // numRows
        nval = nval % 9
        nval = 9 if nval == 0 else nval
        if (x, y) not in nodes:
            nodes[(x, y)] = { "dist": val + nval, "visited": False }
            nodeHeap[(x, y)] = val + nval
        else:
            if val + nval < nodes[(x, y)]["dist"]:
                nodes[(x, y)]["dist"] = val + nval
                nodeHeap[(x, y)] = val + nval

print(nodes[(numRows * n - 1, numCols * n - 1)]["dist"])