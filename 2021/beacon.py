with open("beacon.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

scanners = [[]]

i = 0

for l in range(len(lines)):
    if lines[l].startswith("---"):
        continue
    if len(lines[l]) == 0:
        scanners.append([])
        i += 1
    else:
        x,y,z = lines[l].split(',')
        scanners[i].append((int(x),int(y),int(z)))

def addTuples(t1,t2):
    return (t1[0]+t2[0],t1[1]+t2[1],t1[2]+t2[2])

print([addTuples(scanners[0][i],scanners[0][i]) for i in range(len(scanners[0]))])