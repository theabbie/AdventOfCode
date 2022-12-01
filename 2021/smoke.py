with open("smoke.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

total_risk = 0

numrows = len(lines)
rowlen = len(lines[0])

checked = {}
basins = []

def getNeighbors(i, j):
    neighbors = []
    if i != 0:
        neighbors.append((i - 1, j))
    if i != numrows - 1:
        neighbors.append((i + 1, j))
    if j != 0:
        neighbors.append((i, j - 1))
    if j != rowlen - 1:
        neighbors.append((i, j + 1))
    return neighbors

def check(i, j):
    checked[rowlen * i + j] = True

def isChecked(i, j):
    if rowlen * i + j in checked:
        return True
    return False

def findBasinForLowPoint(i, j):
    basinPoints = [(i, j)]
    k = 0
    while k < len(basinPoints):
        x,y = basinPoints[k]
        currVal = int(lines[x][y])
        neighbors = getNeighbors(x, y)
        for nx, ny in neighbors:
            nval = int(lines[nx][ny])
            if nval != 9 and nval > currVal and (nx, ny) not in basinPoints:
                basinPoints.append((nx, ny))
        k += 1
    return basinPoints

for i in range(numrows):
    for j in range(rowlen):
        if not isChecked(i, j):
            currVal = int(lines[i][j])
            lowPoint = True
            neighbors = getNeighbors(i, j)
            for x,y in neighbors:
                if int(lines[x][y]) <= currVal:
                    lowPoint = False
                    break
                else:
                    check(x, y)
            if lowPoint:
                total_risk += (currVal + 1)
                basinPoints = findBasinForLowPoint(i, j)
                basins.append(len(basinPoints))

basins.sort()

print(total_risk, basins[-1] * basins[-2] * basins[-3])