import inputs
import re

BOARD_SIZE = 5

input = inputs.get(4)
# input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7"""
bingo = [[int(x) for x in re.split("\\s+|,", s.strip())] for s in input.split("\n\n")]

drawings = bingo[0]
boards = bingo[1:]

order = { num: i for i, num in enumerate(drawings) }

def answer(winning):
    min_max = len(drawings) if winning else 0
    winning_board = 0

    for i, board in enumerate(boards):
        candidate = min(min(
            max(order[board[BOARD_SIZE * j + c]] for c in range(BOARD_SIZE)),
            max(order[board[BOARD_SIZE * r + j]] for r in range(BOARD_SIZE))
        ) for j in range(BOARD_SIZE))

        if candidate < min_max if winning else candidate > min_max:
            min_max = candidate
            winning_board = i

    return sum(filter(
        lambda x: order[x] > min_max, boards[winning_board]
    )) * drawings[min_max]

##########
# Part 1 #
##########

print(answer(True))

##########
# Part 2 #
##########

print(answer(False))
