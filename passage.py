with open("passage.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

nodes = {}

for line in lines:
    start,end = line.split("-")

    if start not in nodes:
        nodes[start] = {
            "out": [end]
        }
    else:
        nodes[start]["out"].append(end)

    if end not in nodes:
        nodes[end] = {
            "out": [start]
        }
    else:
        nodes[end]["out"].append(start)

def maxNumberOfTimesASmallCaveWasVisited(currPath):
    numLowerCase = {}
    for node in currPath:
        if node.islower():
            numLowerCase[node] = numLowerCase.get(node, 0) + 1
    return max(numLowerCase.values())

def isValid(node, currPath):
    if node.isupper() or node not in currPath:
        return True
    if node == "start":
        return False
    # Uncomment for Part 2
    # if node.islower() and maxNumberOfTimesASmallCaveWasVisited(currPath) < 2:
    #     return True
    return False

paths = [["start"]]

numPaths = 0

while len(paths) > 0:
    currPath = paths.pop()
    if currPath[-1] == "end":
        # print(",".join(currPath))
        numPaths += 1
        continue
    for node in nodes[currPath[-1]]["out"]:
        if isValid(node, currPath):
            newPath = currPath.copy()
            newPath.append(node)
            paths.append(newPath)

print(numPaths)