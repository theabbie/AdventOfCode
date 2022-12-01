with open("operation.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

precedence = {
    "+": 1,
    "-": 0,
    "*": 0,
    "/": 0
}

def evaluateLTR(expr):
    expr = expr.split()
    operators = []
    operands = []
    for token in expr:
        if token.isdigit():
            operands.append(token)
        elif token in precedence:
            while len(operators) > 0 and precedence[operators[-1]] >= precedence[token]:
                op2 = operands.pop()
                op1 = operands.pop()
                operands.append(str(eval(op1 + operators.pop() + op2)))
            operators.append(token)
    while len(operators) > 0:
        op2 = operands.pop()
        op1 = operands.pop()
        operands.append(str(eval(op1 + operators.pop() + op2)))
    return operands[0]

def evaluate(expr):
    stack = []
    c = 0
    while c < len(expr):
        if expr[c] == "(":
            stack.append(c)
            c += 1
        elif expr[c] == ")":
            beg = stack.pop()
            end = c
            expr = expr[:beg] + evaluateLTR(expr[beg+1:end]) + expr[end+1:]
            c = beg + 1
        else:
            c += 1
    return evaluateLTR(expr)

total = 0

for line in lines:
    total += int(evaluate(line))

print(total)