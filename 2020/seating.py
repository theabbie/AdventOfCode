with open("seating.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

numRows = len(lines)
numCols = len(lines[0])

PART2 = True

minNumOccupied = 5 if PART2 else 4

def getNeighbors(row, col):
    neighbors = []
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if i >= 0 and i < numRows and j >= 0 and j < numCols:
                if i != row or j != col:
                    neighbors.append((i, j))
    return neighbors

def numOccupied(i, j):
    if PART2:
        adj = ""
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx != 0 or dy != 0:
                    n = 1
                    while i + n*dx >= 0 and i + n*dx < numRows and j + n*dy >= 0 and j + n*dy < numCols:
                        if lines[i+dx*n][j+dy*n] != ".":
                            adj += lines[i+dx*n][j+dy*n]
                            break
                        n += 1
        return adj.count("#")
    else:
        neighbors = getNeighbors(i, j)
        return sum(1 if lines[i][j] == '#' else 0 for i, j in neighbors)


while True:
    willBeOccupied = set()
    willBeEmptied = set()
    numChanges = 0
    for i in range(numRows):
        for j in range(numCols):
            curr = lines[i][j]
            if curr != ".":
                num = numOccupied(i, j)
                if curr == 'L' and num == 0:
                    willBeOccupied.add((i, j))
                    numChanges += 1
                if curr == '#' and num >= minNumOccupied:
                    willBeEmptied.add((i, j))
                    numChanges += 1
    for i, j in willBeOccupied:
        lines[i] = lines[i][:j] + '#' + lines[i][j + 1:]
    for i, j in willBeEmptied:
        lines[i] = lines[i][:j] + 'L' + lines[i][j + 1:]
    if numChanges == 0:
        print("".join(lines).count('#'))
        break