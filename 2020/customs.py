with open("customs.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

people = []
total = 0

PART2 = True

for line in lines + [""]:
    if len(line) == 0:
        chunk = set()
        for p in people:
            for c in p:
                chunk.add(c)
        if PART2:
            for p in people:
                chunk = chunk.intersection(set(p))
        total += len(chunk)
        people = []
    else:
        people.append(line)

print(total)