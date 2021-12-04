DEBUG = False

def dprint(*args):
    if DEBUG:
        print("".join(map(str,args)))

filename ="input1.txt"
if DEBUG:
    filename = "test1.txt"

with open(filename) as f:
    file_lines = f.readlines()

def empty_board(board_size):
    return [ [0]*board_size for i in range(board_size)]

def process_raw_lines(lines):

    bingo_calls = list(map(int, lines[0].strip().split(",")))

    remaining_lines = lines[1:]
    boards = []
    board = empty_board(5)
    board_idx = 0
    for line in remaining_lines:
        line = line.strip()
        if line:
            
            board[board_idx] = list(map(int, line.strip().split()))
            board_idx += 1
            if board_idx == 5:
                boards.append(board)
                board = empty_board(5)
                board_idx=0


    return bingo_calls, boards

def mark_board(board, call):
    total = 0
    l = 0
    c = 0
    won = False
    for index_l, line in enumerate(board):
        for index_c, col in enumerate(line):
            if call == col:
                board[index_l][index_c] = "x"

                for i in range(5):
                    if board[index_l][i] == 'x':
                        l += 1
                    if board[i][index_c] == 'x':
                        c += 1
            elif col != 'x':
                total += col
    if l == 5 or c == 5:
        won = True
    return won, total

def part1():
    calls, boards = process_raw_lines(file_lines)
    for call in calls:
        for board in boards:
            won, total = mark_board(board, call)
            if won:
                print("First to win")
                print("Sum: " + str(total) + " Call: " + str(call) + " Answer: " + str(total*call))
                break
        else:  # only execute when it's no break in the inner loop
            continue
        break




def part2():
    calls, boards = process_raw_lines(file_lines)
    total = 0
    for call in calls:
        boards_to_remove = []
        for i, board in enumerate(boards):
            won, total = mark_board(board, call)
            if won:
                boards_to_remove.append(i)
        
        # Just make sure we don't screw up the order while removing boards
        boards_to_remove.reverse()
        for board_idx in boards_to_remove:
            boards.pop(board_idx)
        boards_to_remove = []

        if len(boards) == 0:
            print("Last to win")
            print("Sum: " + str(total) + " Call: " + str(call) + " Answer: " + str(total*call))
            break

part1()
print()
part2()