with open("Gear_Ratios.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

res = 0

m = len(lines)
n = len(lines[0])

counts = [[0] * n for _ in range(m)]
prods = [[1] * n for _ in range(m)]

for i in range(m):
    j = 0
    while j < n:
        ctr = 1
        while j < n - 1 and lines[i][j].isdigit() == lines[i][j + 1].isdigit():
            ctr += 1
            j += 1
        if lines[i][j].isdigit():
            num = int(lines[i][j-ctr+1:j+1])
            valid = False
            for x in range(i - 1, i + 2):
                for y in range(j - ctr, j + 2):
                    if 0 <= x < m and 0 <= y < n and lines[x][y] != "." and not lines[x][y].isdigit():
                        valid = True
                    if 0 <= x < m and 0 <= y < n and lines[x][y] == "*":
                        counts[x][y] += 1
                        prods[x][y] *= num
                        break
            if valid:
                res += num
        j += 1

ratios = 0

for i in range(m):
    for j in range(n):
        if counts[i][j] == 2:
            ratios += prods[i][j]

print(res)
print(ratios)