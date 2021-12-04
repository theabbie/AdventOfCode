with open("sonar.txt") as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]

ctr = 0

for i in range(1, len(lines)):
    if lines[i] > lines[i-1]:
        ctr += 1

print(ctr)

newVals = []
ctr = 0

for i in range(0, len(lines) - 2):
    sum = 0
    for val in lines[i:i+3]:
        sum += val
    if len(newVals) > 0 and sum > newVals[-1]:
        ctr += 1
    newVals.append(sum)

print(ctr)