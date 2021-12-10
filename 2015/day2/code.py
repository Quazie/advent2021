DEBUG = False


def dprint(*args):
    if DEBUG:
        print("".join(map(str, args)))


filename = "input1.txt"
if DEBUG:
    filename = "test1.txt"

with open(filename) as f:
    file_lines = f.readlines()


def process_line(line):
    return list(map(int, line.split("x")))


processed_lines = list(map(process_line, file_lines))


def part1(lines):
    amount = 0
    for line in lines:
        l, w, h = line
        amount += 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, min(l * h, h * w))

    print("Total: " + str(amount))


def part2(lines):
    amount = 0
    for line in lines:
        l, w, h = line
        min_perim = min(2 * l + 2 * h, min(2 * l + 2 * w, 2 * h + 2 * w))
        bow = l * w * h
        amount += min_perim + bow
        dprint("bow: " + str(bow) + " perim: " + str(min_perim))
    print("Total: " + str(amount))


part1(processed_lines)
part2(processed_lines)
