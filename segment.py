with open("segment.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

ctr = 0

def unionOfStrings(str1, str2):
    return "".join(set(str1 + str2))

def differenceOfStrings(str1, str2):
    return "".join(set(str1) - set(str2))

sum = 0

for line in lines:
    signals = line.split(" | ")[0].split(" ")
    output = line.split(" | ")[1].split(" ")
    mappings = {}
    inverse_mappings = [''] * 10
    for segment in signals:
        segment = "".join(sorted(segment))
        if len(segment) == 2:
            mappings[segment] = 1
        elif len(segment) == 3:
            mappings[segment] = 7
        elif len(segment) == 4:
            mappings[segment] = 4
        elif len(segment) == 7:
            mappings[segment] = 8
    for seg in mappings:
        inverse_mappings[mappings[seg]] = seg
    top_char = differenceOfStrings(inverse_mappings[7], inverse_mappings[1])
    top_left_and_middle_char = differenceOfStrings(inverse_mappings[4], inverse_mappings[1])
    bottom_left_and_bottom_char = differenceOfStrings(inverse_mappings[8], inverse_mappings[4] + top_char)
    for segment in signals:
        segment = "".join(sorted(segment))
        if len(segment) == 6:
            if bottom_left_and_bottom_char[0] in segment and bottom_left_and_bottom_char[1] in segment and len(unionOfStrings(inverse_mappings[7], segment)) > 6:
                mappings[segment] = 6
            elif top_left_and_middle_char[0] in segment and top_left_and_middle_char[1] in segment:
                mappings[segment] = 9
            else:
                mappings[segment] = 0
        elif len(segment) == 5:
            if bottom_left_and_bottom_char[0] in segment and bottom_left_and_bottom_char[1] in segment:
                mappings[segment] = 2
            elif top_left_and_middle_char[0] in segment and top_left_and_middle_char[1] in segment:
                mappings[segment] = 5
            else:
                mappings[segment] = 3
    sum += int("".join([str(mappings["".join(sorted(x))]) for x in output]))

print(sum)