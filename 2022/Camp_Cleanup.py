with open("Camp_Cleanup.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

res = 0
overlap = 0

for l in lines:
    ra, rb = l.split(",")
    rax, ray = map(int, ra.split("-"))
    rbx, rby = map(int, rb.split("-"))
    if max(rax, rbx) <= min(ray, rby):
        overlap += 1
    if (rax >= rbx and ray <= rby) or (rbx >= rax and rby <= ray):
        res += 1
    
print(res)
print(overlap)