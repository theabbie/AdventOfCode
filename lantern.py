with open("lantern.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

state = [int(timer) for timer in lines[0].split(",")]
days = 256
MAX = 9

statectr = [0] * MAX

for timer in state:
    statectr[timer] += 1

for i in range(0, days):
    statectrcopy = statectr.copy()
    for i in range(MAX):
        statectr[i] = statectrcopy[(i + 1) % MAX]
    statectr[6] += statectrcopy[0]

print(sum(statectr))