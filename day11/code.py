DEBUG = False


def dprint(*args):
    if DEBUG:
        print(" ".join(map(str, args)))


filename = "input1.txt"
if DEBUG:
    filename = "test1.txt"

with open(filename) as f:
    file_lines = f.readlines()


def process_line(line):
    return list(map(int, line.strip()))


processed_lines = list(map(process_line, file_lines))


def do_flash(flash_point, board, flashed):
    if flash_point not in flashed:
        flashed.append(flash_point)
        to_flash = []
        i, j = flash_point
        for i_diff in [-1, 0, 1]:
            for j_diff in [-1, 0, 1]:
                new_i = i + i_diff
                new_j = j + j_diff
                if not (
                    new_i < 0 or new_j < 0 or new_i >= len(board) or new_j >= len(board)
                ):
                    board[new_i][new_j] += 1
                    if board[new_i][new_j] > 9:
                        to_flash.append((new_i, new_j))

        for new_flash_point in to_flash:
            do_flash(new_flash_point, board, flashed)


def step(board):
    # Step one - increase
    to_flash = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += 1
            if board[i][j] > 9:
                to_flash.append((i, j))

    # flash
    flashed = []
    for flash_point in to_flash:
        do_flash(flash_point, board, flashed)

    for flash_point in flashed:
        i, j = flash_point
        board[i][j] = 0

    return len(flashed)


def both_parts(board):
    count = 0
    for i in range(5000):
        amount = step(board)
        count += amount
        if amount == (len(board) * len(board[0])):
            print(i + 1)
            break

        if i == 99:
            print(count)


both_parts(processed_lines)
