import inputs
import math
import itertools

BIT_STR_LEN = 12

input = inputs.get(3)
diagnostics = [int(x, 2) for x in input.split("\n")]
""" diagnostics = [
    0b00100,
    0b11110,
    0b10110,
    0b10111,
    0b10101,
    0b01111,
    0b00111,
    0b11100,
    0b10000,
    0b11001,
    0b00010,
    0b01010,
] """
count = len(diagnostics)

def most_common_bit(nums, place):
    # Favors 1 over 0 (for part 2).
    return sum((num >> place & 1) * 2 - 1 for num in nums) >= 0

##########
# Part 1 #
##########

gamma = sum(most_common_bit(diagnostics, i) << i for i in range(BIT_STR_LEN))
epsilon = gamma ^ ((1 << BIT_STR_LEN) - 1) # Flip all bits of `gamma`

print(gamma * epsilon)

##########
# Part 2 #
##########

def answer(nums, common):
    for i in reversed(range(BIT_STR_LEN)):
        bit = most_common_bit(nums, i) == common
        nums = list(filter(lambda x : x >> i & 1 == bit, nums))

        if len(nums) <= 1:
            return nums[0]

print(answer(diagnostics, True) * answer(diagnostics, False))
