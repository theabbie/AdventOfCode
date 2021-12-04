with open("binary.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

bs = len(lines[0])
bitctr = [0] * bs
n = len(lines)

for line in lines:
    for i in range(len(line)):
        if line[i] == '1':
            bitctr[i] += 1

gamma = 0
epilson = 0

bitctr.reverse()

for i in range(0, bs):
    if bitctr[i] > n / 2:
        gamma += 2 ** i
    else:
        epilson += 2 ** i

print(gamma * epilson)

lcopy = [line for line in lines]

for i in range(0, bs):
    nn = len([line for line in lines])
    ones = len([line for line in lines if line[i] == '1'])
    if nn == 1:
        break
    if 2 * ones >= nn:
        lines = [line for line in lines if line[i] == '1']
    elif 2 * ones < nn:
        lines = [line for line in lines if line[i] == '0']

for i in range(0, bs):
    nn = len([line for line in lcopy])
    ones = len([line for line in lcopy if line[i] == '1'])
    if nn == 1:
        break
    if 2 * ones >= nn:
        lcopy = [line for line in lcopy if line[i] == '0']
    elif 2 * ones < nn:
        lcopy = [line for line in lcopy if line[i] == '1']

print(int(lines[0], 2) * int(lcopy[0], 2))