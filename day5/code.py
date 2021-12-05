DEBUG = False

def dprint(*args):
    if DEBUG:
        print("".join(map(str,args)))

filename ="input1.txt"
if DEBUG:
    filename = "test1.txt"

with open(filename) as f:
    file_lines = f.readlines()

def process_line(line):
    points = []
    for point in line.strip().split(' -> '):
        
        points.append(list(map(int, point.split(','))))
    return points

processed_lines = list(map(process_line, file_lines))

board = [[0]]

def clear_board():
    global board
    board = [[0]]

def expand_board(x=0, y=0):

    if len(board[0]) < x:
        missing = x - len(board[0])
        for line in board:
            line += ([0]*missing)
    if len(board) < y:
        missing = y - len(board)
        for i in range(missing):
            board.append([0] * len(board[0]))

def mark_line(line, straight_only=False):
    x1, y1 = line[0]
    x2, y2 = line[1]
    expand_board(max(x1,x2)+1, max(y1,y2)+1)

    if x1 == x2 or y1 == y2:
        for x in range(min(x1,x2), max(x1,x2)+1):
            for y in range(min(y1,y2), max(y1,y2)+1):
                board[y][x] += 1
    elif not straight_only:

        ystart = y1 if x1 < x2 else y2
        ydir = 1 if y1 < y2 else -1
        if ystart != y1:
            ydir *= -1
        for i,x in enumerate(range(min(x1,x2), max(x1,x2)+1)):

            board[ystart+(ydir*i)][x] += 1

def count_board(min):
    count = 0
    for line in board:
        for cell in line:
            if cell >= min:
                count += 1
    return count

def part1(lines):
    clear_board()
    for line in lines:
        mark_line(line, straight_only=True)

    print("Straight line crossing points: " + str(count_board(2)))

def part2(lines):
    clear_board()
    for line in lines:      
        mark_line(line)

    print("All line crossing points: " + str(count_board(2)))

part1(processed_lines)
part2(processed_lines)