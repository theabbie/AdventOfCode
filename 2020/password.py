with open("password.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

valid = 0

PART2 = True

for line in lines:
    rawPolicy, rawChar, password = line.split(" ")
    low, high = [int(x) for x in rawPolicy.split("-")]
    char = rawChar[0]
    ctr = password.count(char)
    if PART2:
        if (password[low-1] == char) ^ (password[high-1] == char):
            valid += 1
    else:
        if ctr in range(low, high + 1):
            valid += 1

print(valid)