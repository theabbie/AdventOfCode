with open("segment.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

def unionOfStrings(str1, str2):
    return len(set(str1 + str2))

def differenceOfStrings(str1, str2):
    return len(set(str1) - set(str2))

def sortString(str):
    return "".join(sorted(str))

def sortArrayOfStrings(arr):
    return [sortString(item) for item in arr]

def ArrayToInt(arr):
    return int("".join([str(item) for item in arr]))

sum = 0

for line in lines:
    signals, output = [sortArrayOfStrings(item.split()) for item in line.split(" | ")]
    mappings = {}
    inverse_mappings = [''] * 10
    lenMap = {2: 1, 3: 7, 4: 4, 7: 8}

    for segment in signals:
        seglen = len(segment)
        if seglen not in lenMap:
            continue
        mappings[segment] = lenMap[seglen]
        inverse_mappings[lenMap[seglen]] = segment

    for segment in signals:
        if len(segment) == 6:
            sub7 = differenceOfStrings(segment, inverse_mappings[7])
            sub4 = differenceOfStrings(segment, inverse_mappings[4])

            if sub7 == 4:
                mappings[segment] = 6
            elif sub7 == 3 and sub4 == 2:
                mappings[segment] = 9
            else:
                mappings[segment] = 0

        elif len(segment) == 5:
            add4 = unionOfStrings(segment, inverse_mappings[4])
            add7 = unionOfStrings(segment, inverse_mappings[7])

            if add4 == 7:
                mappings[segment] = 2
            elif add4 == 6 and add7 == 6:
                mappings[segment] = 5
            else:
                mappings[segment] = 3

    sum += ArrayToInt([mappings[x] for x in output])

print(sum)