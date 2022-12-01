with open("hydro.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

BASE = 10000

op = 0
ptctr = {}

def toIndex(x, y):
    return x + y * BASE

def toPoint(index):
    return index % BASE, index // BASE

def smartRange(a, b):
    if a <= b:
        return list(range(a, b + 1))
    else:
        return list(range(a, b - 1, -1))

def getPoints(p1, p2):
    points = []
    xinc = p2[0] - p1[0]
    yinc = p2[1] - p1[1]
    if xinc == 0:
        points = [(p1[0], y) for y in smartRange(p1[1], p2[1])]
    elif yinc == 0:
        points = [(x, p1[1]) for x in smartRange(p1[0], p2[0])]
    elif abs(xinc) == abs(yinc):
        points = [(x, y) for x, y in zip(smartRange(p1[0], p2[0]), smartRange(p1[1], p2[1]))]
    return points

for line in lines:
    p1, p2 = [[int(p) for p in point.split(",")] for point in line.split(" -> ")]
    points = getPoints(p1, p2)
    for x, y in points:
        count = ptctr.get(toIndex(x, y), 0) + 1
        ptctr[toIndex(x, y)] = count
        if count == 2:
            op += 1

print(op)