with open("Rucksack_Reorganization.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

def getpriority(c):
    if ord('a') <= ord(c) <= ord('z'):
        return ord(c) - ord('a') + 1
    elif ord('A') <= ord(c) <= ord('Z'):
        return ord(c) - ord('A') + 27
    return 0

res = 0

for l in lines:
    n = len(l)
    common = set.intersection(set(l[:n//2]), set(l[n//2:]))
    for c in common:
        res += getpriority(c)

print(res)

badgeres = 0

n = len(lines)

for i in range(0, n, 3):
    a, b, c = lines[i], lines[i + 1], lines[i + 2]
    common = set.intersection(set(a), set(b), set(c))
    for c in common:
        badgeres += getpriority(c)

print(badgeres)