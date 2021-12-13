import inputs

UP = "fold along y"
LEFT = "fold along x"

input = inputs.get(13)
# input = """6,10
# 0,14
# 9,10
# 0,3
# 10,4
# 4,11
# 6,0
# 6,12
# 4,1
# 0,13
# 10,12
# 3,4
# 3,0
# 8,4
# 1,10
# 2,14
# 8,10
# 9,0

# fold along y=7
# fold along x=5"""

dots, instructions = (s.split("\n") for s in input.split("\n\n"))
paper = {(int(x), int(y)) for x, y in (line.split(",") for line in dots)}
commands = ((i, int(x)) for i, x in (line.split("=") for line in instructions))

def foldUp(paper, line):
    return set(map(
        lambda x: x if x[1] < line else (x[0], 2 * line - x[1]),
        paper
    ))

def foldLeft(paper, line):
    return set(map(
        lambda x: x if x[0] < line else (2 * line - x[0], x[1]),
        paper
    ))

folds = {
    UP: foldUp,
    LEFT: foldLeft
}

def fold(paper, direction, line):
    return folds[direction](paper, line)

##########
# Part 1 #
##########

first_command = next(commands)
paper = fold(paper, *first_command)

print(len(paper))

##########
# Part 2 #
##########

for command in commands:
    paper = fold(paper, *command)

w = max(paper, key=lambda x: x[0])[0] + 1
h = max(paper, key=lambda x: x[1])[1] + 1

code = [[' ' for _ in range(w)] for _ in range(h)]

for x, y in paper:
    code[y][x] = "#"

print("\n".join(''.join(line) for line in code))
