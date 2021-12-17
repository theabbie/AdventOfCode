with open("adapter.txt") as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]

lines.sort()
used = {}
diffctr = {}
lines = [0] + lines

for line in lines:
    used[line] = False
    
used[lines[-1] + 3] = False

for line in lines:
    for diff in range(1, 4):
        if line + diff in used:
            used[line + diff] = True
            diffctr[diff] = diffctr.get(diff, 0) + 1
            break

print(diffctr[1] * diffctr[3])