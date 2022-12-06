with open("Tuning_Trouble.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

s = lines[0]
n = len(s)

for i in range(n - 3):
    c = s[i:i+4]
    if len(set(c)) == 4:
        print(i+4)
        break

for i in range(n - 13):
    c = s[i:i+14]
    if len(set(c)) == 14:
        print(i+14)
        break