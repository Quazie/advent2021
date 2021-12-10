DEBUG = False


def dprint(*args):
    if DEBUG:
        print("".join(map(str, args)))


filename = "input1.txt"
if DEBUG:
    filename = "test1.txt"

with open(filename) as f:
    file_lines = f.readlines()

processed_lines = []
for line in file_lines:
    processed_lines.append(line.strip().split(" "))


def parse_line(line):
    return line[0], int(line[1])


def part1(lines):
    depth = 0
    pos = 0
    for line in lines:
        command, amount = parse_line(line)

        depth_mult = 1
        if command == "forward":
            pos += amount
        elif command == "up":
            depth_mult = -1

        if command != "forward":
            depth += depth_mult * amount
    print(
        "hor: "
        + str(pos)
        + " depth: "
        + str(depth)
        + " - answer: "
        + (str(pos * depth))
    )


def part2(lines):
    depth = 0
    pos = 0
    aim = 0
    for line in lines:
        command, amount = parse_line(line)

        aim_mult = 1
        if command == "forward":
            pos += amount
            depth += amount * aim
        elif command == "up":
            aim_mult = -1

        if command != "forward":
            aim += aim_mult * amount

    print(
        "hor: "
        + str(pos)
        + " depth: "
        + str(depth)
        + " aim: "
        + str(aim)
        + " - answer: "
        + (str(pos * depth))
    )


part1(processed_lines)
part2(processed_lines)
