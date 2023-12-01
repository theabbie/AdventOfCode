with open("Calorie_Counting.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

maxcals = 0
curr = 0
a, b, c = 0, 0, 0

for l in lines:
    if l == "":
        maxcals = max(maxcals, curr)
        a, b, c = sorted([a, b, c, curr])[1:]
        curr = 0
    else:
        curr += int(l)

maxcals = max(maxcals, curr)
a, b, c = sorted([a, b, c, curr])[1:]

print(maxcals)

print(a + b + c)