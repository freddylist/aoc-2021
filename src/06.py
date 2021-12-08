import inputs

DAYS_1 = 80
DAYS_2 = 256

GROW_TIME = 2
REST_TIME = 7

NEW_TIME = GROW_TIME + REST_TIME

input = inputs.get(6)
# input = "3,4,3,1,2"
initial_fishies = [int(x) for x in input.split(",")]

offsets = [NEW_TIME - x - 1 for x in initial_fishies]

def make_fishies(days):
    generations = [1] * NEW_TIME

    for _ in range(days - NEW_TIME):
        generations.append(generations[-NEW_TIME] + generations[-REST_TIME])

    return generations

fishy_babies = make_fishies(max(DAYS_1, DAYS_2) + max(offsets) + 1)

##########
# Part 1 #
##########

print(sum(fishy_babies[DAYS_1 + x] for x in offsets))

##########
# Part 2 #
##########

print(sum(fishy_babies[DAYS_2 + x] for x in offsets))