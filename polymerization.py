with open("polymerization.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

template = lines[0]
n = len(template)

mappings = {}

ctr = [0] * 26

steps = 3

for i in range(2, len(lines)):
    key, value = lines[i].split(" -> ")
    mappings[key] = value

def incChunk(chunk, k):
    if k < steps:
        newChar = mappings[chunk]
        ctr[ord(newChar) - ord('A')] += 1
        incChunk(chunk[0] + newChar, k + 1)
        incChunk(newChar + chunk[1], k + 1)

for i in range(n - 1):
    chunk = template[i : i + 2]
    incChunk(chunk, 0)

for c in template:
    ctr[ord(c) - ord('A')] += 1

print(ctr)