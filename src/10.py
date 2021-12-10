import inputs
import functools

MATCHING = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

input = inputs.get(10)
# input = """[({(<(())[]>[[{[]{<()<>>
# [(()[<>])]({[<{<<[]>>(
# {([(<{}[<>[]}>{[]{[(<()>
# (((({<>}<{<{<>}{[]{[]{}
# [[<[([]))<([[{}[[()]]]
# [{[{({}]{}}([{[{{{}}([]
# {<[[]]>}<{[{[{[]{()[[[]
# [<(<(<(<{}))><([]([]()
# <{([([[(<>()){}]>(<<{{
# <{([{{}}[<[[[<>{}]]]>[]]"""

lines = input.split("\n")

wrong_closings = []
closing_sequences = []

for line in lines:
    S = []

    for c in line:
        if c in MATCHING:
            S.append(MATCHING[c])
            continue

        if c != S.pop():
            wrong_closings.append(c)
            break
    else:
        closing_sequences.append(''.join(reversed(S)))

##########
# Part 1 #
##########

SYNTAX_SCORES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

print(sum(SYNTAX_SCORES[c] for c in wrong_closings))

##########
# Part 2 #
##########

AUTOCOMPLETE_SCORES = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

def get_score(str):
    return functools.reduce(
        lambda x, y: x * 5 + AUTOCOMPLETE_SCORES[y],
        str,
        0
    )

scores = list(sorted(get_score(s) for s in closing_sequences))

print(scores[len(scores) // 2])