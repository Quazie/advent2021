DEBUG = False


def dprint(*args):
    if DEBUG:
        print("".join(map(str, args)))


filename = "input1.txt"
if DEBUG:
    filename = "test1.txt"

with open(filename) as f:
    lines = f.readlines()

processed_lines = list(map(int, lines))


def part1(lines):
    i = 1
    inc = 0
    while i < len(lines):
        if lines[i] > lines[i - 1]:
            inc += 1
        i += 1
    print("Single increment is " + str(inc))


def part2(lines):
    i = 3
    inc = 0
    while i < len(lines):
        if sum(lines[i - 2 : i + 1]) > sum(lines[i - 3 : i]):
            inc += 1
        i += 1
    print("Rolling increment is " + str(inc))


part1(processed_lines)
part2(processed_lines)
