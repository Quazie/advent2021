DEBUG = True

def dprint(*args):
    if DEBUG:
        print("".join(map(str,args)))

filename ="input1.txt"
if DEBUG:
    filename = "test1.txt"

with open(filename) as f:
    file_lines = f.readlines()

processed_lines = list(map(str, file_lines))

def part1(lines):
    dprint (lines)

def part2(lines):
    dprint (lines)

part1(processed_lines)
part2(processed_lines)