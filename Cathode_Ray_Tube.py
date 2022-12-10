with open("Cathode_Ray_Tube.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

n = len(lines)

cycle = 1
x = 1
res = 0

def isValidCycle(c):
    return (c - 20) % 40 == 0 and c <= 220

M = 6
N = 40
PIXEL = "█"
screen = [[" "] * N for _ in range(M)]

def draw(screen, cycle, x):
    i = (cycle - 1) // 40
    j = (cycle - 1) % 40
    if j in {x - 1, x, x + 1}:
        screen[i][j] = PIXEL

for i in range(n):
    if lines[i] == "noop":
        draw(screen, cycle, x)
        if isValidCycle(cycle):
            res += x * cycle
        cycle += 1
    else:
        c, v = lines[i].split()
        v = int(v)
        if c == "addx":
            for curr in range(2):
                draw(screen, cycle, x)
                if isValidCycle(cycle):
                    res += x * cycle
                if curr == 1:
                    x += v
                cycle += 1

print(res)
print("\n".join("".join(row) for row in screen))