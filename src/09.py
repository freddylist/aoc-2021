import inputs
import itertools
import math

# n-dimensional array helpers:
# (extremely overkill but they were fun to make :D)

def ndenumerate(iterable):
    for i, v in enumerate(iterable):
        try:
            for j, u in ndenumerate(iter(v)):
                yield ((i,) + j, u)
        except TypeError:
            yield ((i,), v)

def in_bounds(m, *x):
    r = x[0]

    return r >= 0 and r < len(m) and (in_bounds(m[r], *x[1:]) if len(x) > 1 else True)

def surrounding(m, *x):
    r = x[0]
    d = x[1:]
    s = tuple((c,) + d for c in (r - 1, r + 1) if in_bounds(m, c, *d))

    return s + tuple(((r,) + c for c in surrounding(m[r], *d)) if len(x) > 1 else ())
    
def ndget(m, *x):
    i = x[0]

    return ndget(m[i], *x[1:]) if len(x) > 1 else m[i]

def surrounding_values(m, *x):
    s = surrounding(m, *x)

    return tuple(ndget(m, *c) for c in s)

input = inputs.get(9)
# input = """2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678"""

lines = input.split("\n")
w = max(len(line) for line in lines)
h = len(lines)
hm = [[int(c) for c in line] for line in lines]

##########
# Part 1 #
##########

risk_level = sum(h + 1 for (r, c), h in ndenumerate(hm) if h < min(surrounding_values(hm, r, c)))

print(risk_level)

##########
# Part 2 #
##########

visited = set()

def flood_size(m, *x, predicate=lambda x: x, visited=None):
    if visited is None:
        visited = set()
    
    if x in visited:
        return 0

    visited.add(x)

    v = ndget(m, *x)

    if not predicate(v):
        return 0

    s = surrounding(m, *x)

    return 1 + sum(flood_size(m, *c, predicate=predicate, visited=visited) for c in s)
    
is_basin = lambda x: x < 9

print(math.prod(itertools.islice(sorted(
    (flood_size(hm, r, c, predicate=is_basin, visited=visited) for (r, c), _ in ndenumerate(hm)),
    reverse=True
), 3)))