from collections import defaultdict, Counter
import inputs
from helpers import pairwise

ITERATIONS = 40

input = inputs.get(14)
# input = """NNCB

# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C"""

polymer, rules = input.split("\n\n")
rules = {p: q for p, q in (line.split(" -> ") for line in rules.split("\n"))}

def step(frequencies):
    stepped = defaultdict(int)

    for (l, r), f in frequencies.items():
        c = rules[l + r]
        stepped[l + c] += f
        stepped[c + r] += f

    return stepped

steps = [Counter(l + r for l, r in pairwise(polymer))]

for i in range(ITERATIONS):
    steps.append(step(steps[i]))

def answer(iteration):
    frequencies = defaultdict(int)

    for (l, r), f in steps[iteration].items():
        frequencies[l] += f
        frequencies[r] += f

    v = frequencies.values()

    # Divide each value by 2 because values are double counted:
    return ((max(v) + 1) // 2 - (min(v) + 1) // 2)

##########
# Part 1 #
##########

print(answer(10))

##########
# Part 2 #
##########

print(answer(40))
