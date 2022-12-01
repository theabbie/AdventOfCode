with open("octopus.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

energies = [[int(energy) for energy in line] for line in lines]

numRows = len(energies)
numCols = len(energies[0])
steps = 100

def printGrid(eg):
    for row in eg:
        print("".join(["{:2}".format(cell) for cell in row]))
    print()

def getNeighbors(row, col):
    neighbors = []
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if i == row and j == col:
                continue
            if i < 0 or i >= numRows:
                continue
            if j < 0 or j >= numCols:
                continue
            neighbors.append((i, j))
    return neighbors

def flash(i, j, flashed):
    flashed[(i, j)] = True
    neighbors = getNeighbors(i, j)
    for x,y in neighbors:
        energies[x][y] += 1
    for x,y in neighbors:
        if energies[x][y] > 9 and (x,y) not in flashed:
            flashed[(x,y)] = True
            flash(x, y, flashed)

totalNumFlashes = 0

printGrid(energies)

step = 0
while True:
    for i in range(numRows):
        for j in range(numCols):
            newEnergy = energies[i][j] + 1
            energies[i][j] = newEnergy

    flashed = {}

    for i in range(numRows):
        for j in range(numCols):
            if energies[i][j] > 9 and (i,j) not in flashed:
                flash(i, j, flashed)

    totalNumFlashes += len(flashed)
    
    for i in range(numRows):
        for j in range(numCols):
            if energies[i][j] > 9:
                energies[i][j] = 0

    printGrid(energies)
    step += 1

    # PART 1
    # if step == steps:
    #     break

    if sum(sum(row) for row in energies) == 0:
        print("Step:", step)
        break

print(totalNumFlashes)