import inputs

SIZE = 10_000

def get_line(s):
    a, b = s.split(" -> ")

    x1, y1 = (int(x) for x in a.split(","))
    x2, y2 = (int(x) for x in b.split(","))

    return ((x1, y1), (x2, y2))

input = inputs.get(5)
lines = [get_line(s) for s in input.split("\n")]
""" lines = [
    ((0, 9), (5, 9)),
    ((8, 0), (0, 8)),
    ((9, 4), (3, 4)),
    ((2, 2), (2, 1)),
    ((7, 0), (7, 4)),
    ((6, 4), (2, 0)),
    ((0, 9), (2, 9)),
    ((3, 4), (1, 4)),
    ((0, 0), (8, 8)),
    ((5, 5), (8, 2)),
] """

# Part 1 densities
d1 = {}

# Part 2 densities
d2 = {}

for line in lines:
    a, b = line
    x1, y1 = a
    x2, y2 = b

    dx = x2 - x1
    dy = y2 - y1

    start = y1 * SIZE + x1
    stop = y2 * SIZE + x2
    dif = stop - start
    steps = max(abs(dx), abs(dy))

    for i in range(start, stop + (dif > 0) * 2 - 1, dif // steps):
        d2[i] = d2.get(i, 0) + 1

        if x1 == x2 or y1 == y2:
            d1[i] = d1.get(i, 0) + 1

##########
# Part 1 #
##########

print(sum(x > 1 for x in d1.values()))

##########
# Part 2 #
##########

print(sum(x > 1 for x in d2.values()))