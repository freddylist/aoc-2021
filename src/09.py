from itertools import islice
import math
import inputs
from helpers import deep_enumerate, surrounding, flood_fill

input = inputs.get(9)
# input = """2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678"""

hm = [[int(c) for c in line] for line in input.split("\n")]

##########
# Part 1 #
##########

risk_level = sum(
    h + 1 for (r, c), h in deep_enumerate(hm) if h < min(surrounding(hm, (r, c)).values())
)

print(risk_level)

##########
# Part 2 #
##########

is_basin = lambda x: x < 9
visited = set()
basin_sizes = []

for p, _ in deep_enumerate(hm):
    if p not in visited:
        flood = flood_fill(hm, p, is_basin)
        visited |= set(flood)
        basin_sizes.append(len(flood))

print(math.prod(islice(sorted(basin_sizes, reverse=True), 3)))