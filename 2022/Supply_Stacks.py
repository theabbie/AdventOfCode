from collections import defaultdict, deque
import re

with open("Supply_Stacks.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

x = 0

while not lines[x].startswith("move"):
    x += 1

stacks = defaultdict(list)

for i in range(x - 3, -1, -1):
    n = len(lines[i])
    if n != 0:
        for j in range(n):
            if j < len(lines[x- 2]) and lines[x - 2][j] != " " and lines[i][j] != " ":
                stacks[lines[x - 2][j]].append(lines[i][j])

PART1 = False

for i in range(x, len(lines)):
    command = re.search("move (\d+) from (\d+) to (\d+)", lines[i])
    n, u, v = command.group(1),command.group(2), command.group(3)
    if PART1:
        for _ in range(int(n)):
            stacks[v].append(stacks[u].pop())
    else:
        curr = deque()
        for _ in range(int(n)):
            curr.append(stacks[u].pop())
        for _ in range(int(n)):
            stacks[v].append(curr.pop())

print("".join(stacks[i][-1] for i in lines[x - 2].split()))