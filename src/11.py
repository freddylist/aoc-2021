import itertools
import inputs
from helpers import deep_get, deep_set, deep_enumerate, deep_update, surrounding

ITERATIONS = 100

input = inputs.get(11)
# input = """5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526"""

increase = lambda x: x + 1

def step(energies, octopus, flashed=None):
    if flashed is None:
        flashed = set()

    if octopus in flashed:
        return 0

    energy = deep_update(energies, octopus, increase)

    if energy <= 9:
        return 0

    flashed.add(octopus)

    deep_set(energies, octopus, 0)

    s = surrounding(energies, octopus, diagonals=True)

    return 1 + sum(
        step(energies, p, flashed=flashed) for p in s.keys()
    )

##########
# Part 1 #
##########

energies = [[int(x) for x in line] for line in input.split("\n")]
flashes = 0

for i in range(ITERATIONS):
    flashed = set()
    flashes += sum(
        step(energies, p, flashed) for p, _ in deep_enumerate(energies)
    )

print(flashes)

##########
# Part 2 #
##########

# Assuming flashes aren't synchronized from last simulation,
# we can start from the last iteration:
for i in itertools.count(start=ITERATIONS):
    synced = True
    flashed = set()
    v = energies[0][0]

    for p, e in deep_enumerate(energies):
        step(energies, p, flashed)
        synced &= v == e

    if synced:
        print(i)
        break
