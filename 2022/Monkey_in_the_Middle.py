from collections import deque
import re

with open("Monkey_in_the_Middle.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

LCM = 1

class Monkey:
    def __init__(self, items, operation, div, a, b):
        self.items = deque(items)
        self.operation = lambda x, d: eval(operation.replace("old", str(x))) // d
        self.next = lambda x: a if x % div == 0 else b
        self.ctr = 0

    def catch(self, item):
        self.items.append(item % LCM)

    def inspect(self, throw, d):
        while len(self.items) > 0:
            curr = self.items.popleft()
            worry = self.operation(curr, d)
            receiver = self.next(worry)
            throw(receiver, worry)
            self.ctr += 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

monkeys = []

for i in range(0, len(lines), 7):
    m = re.search("Monkey (\d+):", lines[i]).group(1)
    items = re.search("Starting items: (.*)", lines[i + 1]).group(1).split(", ")
    operation = re.search("Operation: new = (.*)", lines[i + 2]).group(1)
    div = re.search("Test: divisible by (\d+)", lines[i + 3]).group(1)
    a = re.search("If true: throw to monkey (\d+)", lines[i + 4]).group(1)
    b = re.search("If false: throw to monkey (\d+)", lines[i + 5]).group(1)
    m, div, a, b, items = int(m), int(div), int(a), int(b), list(map(int, items))
    LCM = LCM * div // gcd(LCM, div)
    monkeys.append(Monkey(items, operation, div, a, b))

def throw(receiver, worry):
    monkeys[receiver].catch(worry)

PART1 = True

if PART1:
    LCM = float('inf')
    for round in range(20):
        for m in monkeys:
            m.inspect(throw, 3)
else:
    for round in range(10000):
        for m in monkeys:
            m.inspect(throw, 1)

a = b = 0
for m in monkeys:
    temp, a, b = sorted([a, b, m.ctr])

print(a * b)