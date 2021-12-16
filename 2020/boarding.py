with open("boarding.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

maxSeatId = 0

unusedSeats = {}

for i in range(128 * 8):
    unusedSeats[i + 1] = True

for line in lines:
    rawRow = line[:7]
    rawCol = line[7:]
    row = 0
    col = 0
    for cell in rawRow:
        row = 2 * row + (0 if cell == "F" else 1)
    for cell in rawCol:
        col = 2 * col + (0 if cell == "L" else 1)
    seatId = 8 * row + col
    del unusedSeats[seatId]
    if seatId > maxSeatId:
        maxSeatId = seatId

print(maxSeatId, unusedSeats.keys())