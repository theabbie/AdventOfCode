with open("passport.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

chunk = []
ctr = 0

def validate(currChunk):
    requiredKeys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    fields = {}
    for line in currChunk:
        for rawKeyValue in line.split(" "):
            key, value = rawKeyValue.split(":")
            fields[key] = value
    for key in requiredKeys:
        if key not in fields:
            return False
    if not fields["byr"].isdigit() or 1920 <= int(fields["byr"]) <= 2002:
        return False
    if not fields["iyr"].isdigit() or 2010 <= int(fields["iyr"]) <= 2020:
        return False
    if not fields["eyr"].isdigit() or 2020 <= int(fields["iyr"]) <= 2030:
        return False
    return True

for line in lines:
    if len(line) == 0:
        if validate(chunk):
            ctr += 1
        chunk = []
        continue
    else:
        chunk.append(line)

print(ctr)