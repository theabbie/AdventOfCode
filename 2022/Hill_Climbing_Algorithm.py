from collections import deque

with open("Hill_Climbing_Algorithm.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

lines = list(map(list, lines))

def minsteps(beg, cmp, target = None, targetchr = None):
    res = float('inf')
    q = deque([(beg[0], beg[1], 0)])
    v = {beg}
    while len(q) > 0:
        i, j, d = q.pop()
        if (i, j) == target or lines[i][j] == targetchr:
            res = min(res, d)
        for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
            if 0 <= x < m and 0 <= y < n and (x, y) not in v and cmp(lines[i][j], lines[x][y]):
                v.add((x, y))
                q.appendleft((x, y, d + 1))
    return res

m = len(lines)
n = len(lines[0])
beg = target = None

for i in range(m):
    for j in range(n):
        if lines[i][j] == "S":
            beg = (i, j)
            lines[i][j] = "a"
        if lines[i][j] == "E":
            target = (i, j)
            lines[i][j] = "z"

print(minsteps(beg, lambda a, b: ord(b) <= ord(a) + 1, target))
print(minsteps(target, lambda a, b: ord(b) >= ord(a) - 1, None, 'a'))