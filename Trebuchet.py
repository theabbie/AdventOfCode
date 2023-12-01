with open("Trebuchet.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

PARTONE = False

if PARTONE:
    res = 0

    for l in lines:
        first_digit = last_digit = None
        for c in l:
            if c.isdigit():
                if first_digit == None:
                    first_digit = int(c)
                last_digit = int(c)
        res += 10 * first_digit + last_digit

    print(res)

res = 0

words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for l in lines:
    first_digit = last_digit = None
    n = len(l)
    for i in range(n):
        d = None
        if l[i].isdigit():
            d = int(l[i])
        else:
            for j in range(9):
                if i + len(words[j]) <= n and l[i:i+len(words[j])] == words[j]:
                    d = j + 1
                    break
        if d != None:
            if first_digit == None:
                first_digit = d
            last_digit = d
    res += 10 * first_digit + last_digit

print(res)