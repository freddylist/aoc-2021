import inputs
import itertools

def sliding_window(iterable, size):
    it = iter(iterable)
    window = tuple(itertools.islice(it, size))

    if len(window) == size:
        yield window
    for x in it:
        window = window[1:] + (x,)
        
        yield window

def num_increases(values):
    return sum(b > a for a, b in sliding_window(values, 2))

input = inputs.get(1)
sonar_scan = [int(x) for x in input.split("\n")]
""" sonar_scan = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263] """

##########
# Part 1 #
##########

print(num_increases(sonar_scan))

##########
# Part 2 #
##########

WINDOW_SIZE = 3

print(num_increases(sum(window) for window in sliding_window(sonar_scan, WINDOW_SIZE)))
