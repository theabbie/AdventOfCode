with open("cubes.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

pad = 10

edge = len(lines[0]) + 2 * pad

cycles = 6

cube = [[[[0 for i in range(edge)] for j in range(edge)] for k in range(edge)] for l in range(edge)]

def cubeIter(ri=range(edge), rj=range(edge), rk=range(edge), rl=range(edge)):
    for i in ri:
        for j in rj:
            for k in rk:
                for l in rl:
                    yield i, j, k, l

for i, j, k, l in cubeIter():
    if k != edge // 2 or l != edge // 2:
        continue
    if i in range(pad, edge - pad) and j in range(pad, edge - pad):
        if lines[i - pad][j - pad] == '#':
            cube[i][j][k][l] = 1

def getNeighbors(x, y, z, w):
    neighbors = []
    for i, j, k, l in cubeIter(range(x-1, x+2), range(y-1, y+2), range(z-1, z+2), range(w-1, w+2)):
        if i == x and j == y and k == z and l == w:
            continue
        if i < 0 or i >= edge or j < 0 or j >= edge or k < 0 or k >= edge or l < 0 or l >= edge:
            continue
        neighbors.append((i, j, k, l))
    return neighbors

for _ in range(cycles):
    mustSwitch = set()
    for i, j, k, l in cubeIter():
        curr = cube[i][j][k][l]
        neighbors = getNeighbors(i, j, k, l)
        numActiveNeighbours = sum([cube[x][y][z][w] for x, y, z, w in neighbors])
        if curr == 0 and numActiveNeighbours == 3:
            mustSwitch.add((i, j, k, l))
        elif curr == 1 and numActiveNeighbours != 2 and numActiveNeighbours != 3:
            mustSwitch.add((i, j, k, l))
    for i, j, k, l in mustSwitch:
        cube[i][j][k][l] = 1 - cube[i][j][k][l]

total = 0

for i, j, k, l in cubeIter():
    total += cube[i][j][k][l]

print(total)