import inputs

BIT_STR_LEN = 12

input = inputs.get(3)
# input = """00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010"""
diagnostics = [int(x, 2) for x in input.split("\n")]
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
        nums = list(filter(lambda x: x >> i & 1 == bit, nums))

        if len(nums) <= 1:
            return nums[0]

print(answer(diagnostics, True) * answer(diagnostics, False))
