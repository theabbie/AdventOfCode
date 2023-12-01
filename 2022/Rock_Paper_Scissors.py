with open("Rock_Paper_Scissors.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

res = 0

resalt = 0

draw = {("A", "X"), ("B", "Y"), ("C", "Z")}
lose = {("A", "Z"), ("B", "X"), ("C", "Y")}
score = {"X": 1, "Y": 2, "Z": 3}
scoretowin = {"A": 2, "B": 3, "C": 1}
scoretolose = {"A": 3, "B": 1, "C": 2}
scoretodraw = {"A": 1, "B": 2, "C": 3}

for l in lines:
    a, b = l.split()
    res += score[b]
    if (a, b) in draw:
        res += 3
    elif (a, b) not in lose:
        res += 6
    if b == "X":
        resalt += scoretolose[a]
    elif b == "Y":
        resalt += scoretodraw[a] + 3
    else:
        resalt += scoretowin[a] + 6

print(res)

print(resalt)
