from itertools import chain, product, permutations
import inputs

input = inputs.get(8)

# input = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
# edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
# fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
# fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
# aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
# fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
# dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
# bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
# egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
# gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

# input = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"

signals = [tuple(s.split(" ") for s in l.split(" | ")) for l in input.split("\n")]

##########
# Part 1 #
##########

unique_len = { 2, 3, 4, 7 }

print(sum(len(s) in unique_len for s in chain.from_iterable(d for _, d in signals)))

##########
# Part 2 #
##########

CORRECT_PATTERNS = [
    "abcefg", "cf", "acdeg", "acdfg", "bcdf",
    "abdfg", "abdefg", "acf", "abcdefg", "abcdfg",
]
SEGMENTS = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
NUM_SEGMENTS = max(SEGMENTS)

segment_bitmasks = {c: 1 << i for i, c in enumerate("abcdefg")}
identity_bitmask = (1 << NUM_SEGMENTS) - 1

def to_bits(pattern):
    return sum(segment_bitmasks[c] for c in pattern)

bit_pattern_map = {to_bits(p): i for i, p in enumerate(CORRECT_PATTERNS)}
correct_bit_patterns = [to_bits(p) for p in CORRECT_PATTERNS]

def rewire(bit_pattern, wirings):
    return sum(w for i, w in enumerate(wirings) if (1 << i) & bit_pattern)

def read(output, wirings):
    return sum(
        bit_pattern_map[rewire(to_bits(p), wirings)] * 10 ** i for i, p in enumerate(reversed(output))
    )

def solve(patterns, output):
    by_length = {s: [] for s in SEGMENTS}

    for p in patterns:
        by_length[len(p)].append(to_bits(p))

    for arrangement in product(*(by_length[s] for s in SEGMENTS)):
        wirings = [identity_bitmask] * NUM_SEGMENTS

        for i, p in enumerate(arrangement):
            cp = correct_bit_patterns[i]

            for j in range(NUM_SEGMENTS):
                wirings[j] &= cp if (1 << j) & p else cp ^ identity_bitmask

        if all(w and not w & (w - 1) for w in wirings):
            return read(output, wirings)

print(sum(solve(p, d) for p, d in signals))

# Alternative method (slower, I think... too lazy to test :P):

def solve2(patterns, output):
    for wirings in permutations(segment_bitmasks.values()):
        rewired = (rewire(to_bits(p), wirings) for p in patterns)

        if all(p in bit_pattern_map for p in rewired):
            return read(output, wirings)

print(sum(solve2(p, d) for p, d in signals))