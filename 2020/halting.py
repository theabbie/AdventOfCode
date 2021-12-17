with open("halting.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

insn = [(lines[i][:3], int(lines[i][4:])) for i in range(len(lines))]

jmps = [i for i in range(len(insn)) if insn[i][0] == "jmp"]

curr = 0
acc = 0
switch = 0

while switch < len(jmps):
    acc = 0
    visited = {}
    curr = 0
    while curr < len(lines) and curr not in visited and curr < len(lines):
        visited[curr] = True
        ins, arg = insn[curr]
        if ins == "acc":
            acc += arg
        elif ins == "jmp" and curr != jmps[switch]:
            curr += arg
            continue
        curr += 1
    if curr >= len(lines):
        break
    switch += 1

print(acc)