with open("dive.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

x = 0
y = 0

for line in lines:
    if line[0:7] == "forward":
        x += int(line[8:])
    if line[0:4] == "down":
        y += int(line[5:])
    if line[0:2] == "up":
        y -= int(line[3:])

print(x*y)

x = 0
y = 0
aim = 0

for line in lines:
    if line[0:7] == "forward":
        x += int(line[8:])
        y += int(line[8:]) * aim
    if line[0:4] == "down":
        aim += int(line[5:])
    if line[0:2] == "up":
        aim -= int(line[3:])

print(x*y)