with open("Treetop_Tree_House.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

m = len(lines)
n = len(lines[0])

vis = [[False] * n for _ in range(m)]

for i in range(m):
    maxyet = float('-inf')
    for j in range(n):
        if int(lines[i][j]) > maxyet:
            vis[i][j] = True
        maxyet = max(maxyet, int(lines[i][j]))
    maxyet = float('-inf')
    for j in range(n - 1, -1, -1):
        if int(lines[i][j]) > maxyet:
            vis[i][j] = True
        maxyet = max(maxyet, int(lines[i][j]))

for j in range(n):
    maxyet = float('-inf')
    for i in range(m):
        if int(lines[i][j]) > maxyet:
            vis[i][j] = True
        maxyet = max(maxyet, int(lines[i][j]))
    maxyet = float('-inf')
    for i in range(m - 1, -1, -1):
        if int(lines[i][j]) > maxyet:
            vis[i][j] = True
        maxyet = max(maxyet, int(lines[i][j]))

res = 0
for i in range(m):
    for j in range(n):
        if vis[i][j]:
            res += 1

print(res)

score = [[1] * n for _ in range(m)]

for i in range(m):
    stack = []
    for j in range(n):
        while len(stack) > 0 and int(lines[i][stack[-1]]) <= int(lines[i][j]):
            curr = stack.pop()
            score[i][curr] *= j - curr
        stack.append(j)
    while len(stack) > 0:
        curr = stack.pop()
        score[i][curr] *= n - curr - 1
    for j in range(n - 1,- 1, -1):
        while len(stack) > 0 and int(lines[i][stack[-1]]) <= int(lines[i][j]):
            curr = stack.pop()
            score[i][curr] *= curr - j
        stack.append(j)
    while len(stack) > 0:
        curr = stack.pop()
        score[i][curr] *= curr
    
for j in range(n):
    stack = []
    for i in range(m):
        while len(stack) > 0 and int(lines[stack[-1]][j]) <= int(lines[i][j]):
            curr = stack.pop()
            score[curr][j] *= i - curr
        stack.append(i)
    while len(stack) > 0:
        curr = stack.pop()
        score[curr][j] *= m - curr - 1
    for i in range(m - 1,- 1, -1):
        while len(stack) > 0 and int(lines[stack[-1]][j]) <= int(lines[i][j]):
            curr = stack.pop()
            score[curr][j] *= curr - i
        stack.append(i)
    while len(stack) > 0:
        curr = stack.pop()
        score[curr][j] *= curr

maxscore = 0
for i in range(m):
    for j in range(n):
        maxscore = max(maxscore, score[i][j])

print(maxscore)