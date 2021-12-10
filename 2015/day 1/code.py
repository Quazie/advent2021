DEBUG = True


def dprint(*args):
    if DEBUG:
        print("".join(map(str, args)))


filename = "input1.txt"
if DEBUG:
    filename = "test1.txt"

with open(filename) as f:
    file_lines = f.readlines()

processed_line = file_lines[0].strip()


def part1(line):
    floor = 0
    for char in line:
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
        else:
            print("What is " + char)
    print("Floor: " + str(floor))


def part2(line):
    floor = 0
    for i, char in enumerate(line):
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
        else:
            print("What is " + char)

        if floor < 0:
            print("basement at: " + str(i + 1))
            break


part1(processed_line)
part2(processed_line)
