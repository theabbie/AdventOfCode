with open("Rope_Bridge.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

def getneighbours(i, j, diag = False):
    res = set()
    for p in range(i - 1, i + 2):
        for q in range(j - 1, j + 2):
            if not diag or (p != i and q != j):
                res.add((p, q))
    return res

def getmove(x, y, command):
    if command == 'U':
        return (x, y - 1)
    elif command == 'D':
        return (x, y + 1)
    elif command == 'L':
        return (x - 1, y)
    elif command == 'R':
        return (x + 1, y)

def gettail(x, y, tx, ty):
    fav = getneighbours(x, y)
    if (tx, ty) in fav:
        return (tx, ty)
    if x == tx:
        if y > ty:
            return (x, y - 1)
        return (x, y + 1)
    elif y == ty:
        if x > tx:
            return (x - 1, y)
        return (x + 1, y)
    return min(getneighbours(tx, ty, True), key = lambda p: 0 if p in fav else 1)

def simulate(K):
    pos = [(0, 0)] * K
    v = {pos[0]}
    for l in lines:
        command, d = l.split()
        d = int(d)
        for _ in range(d):
            pos[K - 1] = getmove(pos[K - 1][0], pos[K - 1][1], command)
            for i in range(K - 2, -1, -1):
                pos[i] = gettail(pos[i + 1][0], pos[i + 1][1], pos[i][0], pos[i][1])
            v.add(pos[0])
    return len(v)

print(simulate(2))
print(simulate(10))