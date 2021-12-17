with open("origami.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

points = []
xfolds = []
yfolds = []

maxX = 0
maxY = 0

for line in lines:
    if len(line) > 0:
        if line.startswith("fold along"):
            type, val = line[11:].split("=")
            if type == "x":
                xfolds.append(int(val))
            elif type == "y":
                yfolds.append(int(val))
        else:
            x, y = line.split(",")
            points.append((int(x), int(y)))
            maxX = max(maxX, int(x))
            maxY = max(maxY, int(y))

dimX = min(xfolds) if len(xfolds) > 0 else maxX + 1
dimY = min(yfolds) if len(yfolds) > 0 else maxY + 1       

op = [[0 for x in range(dimX)] for y in range(dimY)]

for point in points:
    x,y = point
    for yaxis in yfolds:
        y = yaxis - abs(y - yaxis)
    for xaxis in xfolds:
        x = xaxis - abs(x - xaxis)
    if x < 0 or y < 0:
        continue
    op[y][x] = 1

print(sum(sum(row) for row in op))

print("\n".join(["".join(["█" if x else " " for x in row]) for row in op]))