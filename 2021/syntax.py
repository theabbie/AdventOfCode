with open("syntax.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

scoreMap = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

autoCompleteScoreMap = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

bracketPairs = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

def isOpeningBracket(char):
    return char in ["(", "[", "{", "<"]

def isClosingBracket(char):
    return char in [")", "]", "}", ">"]

def isBracketPair(opening, closing):
    if (opening, closing) in [("(", ")"), ("[", "]"), ("{", "}"), ("<", ">")]:
        return True
    return False

total_score = 0
autocomplete_scores = []

for line in lines:
    stack = []
    score = 0
    autocomplete_score = 0
    isIncomplete = True
    for char in line:
        if isOpeningBracket(char):
            stack.append(char)
        if isClosingBracket(char):
            if not isBracketPair(stack[-1], char):
                isIncomplete = False
                score = scoreMap[char]
                break
            else:
                stack.pop()
    if not isIncomplete:
        total_score += score
    else:
        while len(stack) > 0:
            currScore = autoCompleteScoreMap[bracketPairs[stack.pop()]]
            autocomplete_score = 5 * autocomplete_score + currScore
        autocomplete_scores.append(autocomplete_score)
    
autocomplete_scores.sort()
numScores = len(autocomplete_scores)

print(total_score, autocomplete_scores[numScores // 2])