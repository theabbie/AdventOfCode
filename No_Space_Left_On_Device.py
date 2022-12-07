with open("No_Space_Left_On_Device.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

currdir = [""]
ls = True
tree = {"": {}}

for l in lines:
    if l.startswith("$ "):
        if l.startswith("$ cd "):
            ls = False
            d = l[5:]
            if d == "/":
                currdir = [""]
            elif d == "..":
                if len(currdir) > 1:
                    currdir.pop()
            else:
                currdir.append(d)
        elif l.startswith("$ ls"):
            ls = True
    else:
        if ls:
            curr = tree
            for f in currdir:
                if f not in curr:
                    curr[f] = {}
                curr = curr[f]
            if l.startswith("dir "):
                name = l[4:]
                curr[name] = {}
            else:
                s, name = l.split()
                curr[name] = int(s)
    
sizes = {}

def size(tree, path):
    res = 0
    for f in tree:
        if isinstance(tree[f], int):
            res += tree[f]
        else:
            res += size(tree[f], path + "/" + f)
    sizes[path] = res
    return res

size(tree, "")

res = 0

for f in sizes:
    if sizes[f] <= 100000:
        res += sizes[f]

print(res)

M = 70000000
required = max(30000000 - M + sizes[""], 0)

mindir = float('inf')

for f in sizes:
    if sizes[f] >= required:
        mindir = min(mindir, sizes[f])

print(mindir)