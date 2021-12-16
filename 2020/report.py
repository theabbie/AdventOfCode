with open("report.txt") as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]

n = 3 # 2 for part 1
target = 2020

for line in lines:
    nums = [[ line ]]
    while len(nums) > 0:
        currNums = nums.pop()
        if len(currNums) == n and sum(currNums) == target:
            print(currNums)
            product = 1
            for num in currNums:
                product *= num
            print(product)
            continue
        for num in lines:
            if num not in currNums and num <= target - sum(currNums):
                nums.append(currNums + [num])