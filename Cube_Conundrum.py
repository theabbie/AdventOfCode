with open("Cube_Conundrum.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

MAXRED = 12
MAXGREEN = 13
MAXBLUE = 14

res = 0
powers = 0

for line in lines:
    sep = line.index(":")
    ID = int(line[:sep].split(" ")[1])
    counts = line[sep+1:].split(";")
    valid = True
    mred = 0
    mblue = 0
    mgreen = 0
    for ctr in counts:
        curr = ctr.split(",")
        for ball in curr:
            count, color = ball.strip().split(" ")
            count = int(count)
            if color == "red":
                if count > MAXRED:
                    valid = False
                mred = max(mred, count)
            if color == "blue":
                if count > MAXBLUE:
                    valid = False
                mblue = max(mblue, count)
            if color == "green":
                if count > MAXGREEN:
                    valid = False
                mgreen = max(mgreen, count)
    if valid:
        res += ID
    powers += mred * mblue * mgreen

print(res)
print(powers)