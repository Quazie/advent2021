DEBUG = False


def dprint(*args):
    if DEBUG:
        print(" ".join(map(str, args)))


filename = "input1.txt"
if DEBUG:
    filename = "test1.txt"

with open(filename) as f:
    file_lines = f.readlines()

dots = []
folds = []
for line in file_lines:
    test = line.strip().split(",")
    if len(test) == 2:
        dots.append(list(map(int, test)))
    else:
        test = test[0][11:].split("=")
        if len(test) == 2:
            folds.append(test)

board = [[0]]


def expand_board(x=0, y=0):

    if len(board[0]) < x:
        missing = x - len(board[0])
        for line in board:
            line += [0] * missing
    if len(board) < y:
        missing = y - len(board)
        for _ in range(missing):
            board.append([0] * len(board[0]))


def shrink_board(fold):
    global board
    axis, amount = fold
    amount = int(amount)
    if axis == "y":
        board = board[:amount]
    else:
        for i in range(len(board)):
            board[i] = board[i][:amount]


def folding(dots, folds):

    for dot in dots:
        x, y = dot
        expand_board(x + 1, y + 1)
        board[y][x] = 1
    for fold_i, fold in enumerate(folds):
        where = int(fold[1])

        if fold[0] == "y":
            for idx, i in enumerate(range(where + 1, len(board))):
                new_idx = where - 1 - idx
                for x in range(len(board[0])):
                    board[new_idx][x] = board[new_idx][x] or board[i][x]
                    board[i][x] = 0

        else:
            for idx, i in enumerate(range(where + 1, len(board[0]))):
                new_idx = where - 1 - idx
                for y in range(len(board)):
                    board[y][new_idx] = board[y][new_idx] or board[y][i]
                    board[y][i] = 0
        shrink_board(fold)
        dprint(len(board))

        if fold_i == 0:
            total = 0
            for line in board:
                total += sum(line)
            dprint(board)
            print(total)

    # Print board for human consumption
    for i, line in enumerate(board):
        for j, char in enumerate(line):
            if char:
                board[i][j] = "#"
            else:
                board[i][j] = " "
    for line in board:
        print("".join(line))


folding(dots, folds)
