import inputs
from helpers import pairwise, sliding_window

def num_increases(values):
    return sum(b > a for a, b in pairwise(values))

input = inputs.get(1)
# input = """199
# 200
# 208
# 210
# 200
# 207
# 240
# 269
# 260
# 263"""
sonar_scan = [int(x) for x in input.split("\n")]

##########
# Part 1 #
##########

print(num_increases(sonar_scan))

##########
# Part 2 #
##########

WINDOW_SIZE = 3

print(num_increases(sum(window) for window in sliding_window(sonar_scan, WINDOW_SIZE)))
