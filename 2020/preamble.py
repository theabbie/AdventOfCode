with open("preamble.txt") as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]

n = 25
window = lines[:n]

possiblePairSums = []

encSum = 0

for a in range(n):
    for b in range(n):
        if a != b:
            possiblePairSums.append(window[a] + window[b])

for l in range(n, len(lines)):
    if lines[l] not in possiblePairSums:
        encSum = lines[l]
        break
    for i in range(n - 1):
        possiblePairSums.pop(0)
    window.pop(0)
    for oldSum in window:
        possiblePairSums.append(oldSum + lines[l])
    window.append(lines[l])

beg = 0
width = 2

while sum(lines[beg:beg + width]) != encSum:
    width += 1
    if beg + width > len(lines):
        beg += 1
        width = 2

print(min(lines[beg:beg + width]) + max(lines[beg:beg + width]))