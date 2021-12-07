import inputs
import math

input = inputs.get(7)
positions = [int(x) for x in input.split(",")]
#positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

positions.sort()

##########
# Part 1 #
##########

median = positions[len(positions) // 2]

print(sum(abs(x - median) for x in positions))

##########
# Part 2 #
##########

# https://en.wikipedia.org/wiki/Golden_ratio
GOLDEN_RATIO = 1.618_033_988_749

def gr_round(n):
    return math.floor(n + 2 - GOLDEN_RATIO)

average = gr_round(sum(positions) / len(positions))

print(sum(d * (d + 1) // 2 for d in (abs(x - average) for x in positions)))

"""
I figured that the alignment position for part 2 would be the average of all
positions.

However, I have no idea why it is rounded around the decimal part of the golden
ratio. I came to that conclusion by inspecting the average of different sets of
positions.
"""