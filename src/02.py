import inputs

def parse(expression):
    name, distance = expression.split(" ")

    return (name, int(distance))

input = inputs.get(2)
directions = [parse(expression) for expression in input.split("\n")]
""" directions = [
    ("forward", 5),
    ("down", 5),
    ("forward", 8),
    ("up", 3),
    ("down", 8),
    ("forward", 2),
] """

##########
# Part 1 #
##########

depth = 0
position = 0

for command, distance in directions:
    if command == "forward":
        position += distance
    elif command == "up":
        depth -= distance
    elif command == "down":
        depth += distance

print(depth * position)

##########
# Part 2 #
##########

depth = 0
position = 0
aim = 0

for command, distance in directions:
    if command == "forward":
        position += distance
        depth += aim * distance
    elif command == "up":
        aim -= distance
    elif command == "down":
        aim += distance

print(depth * position)
