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
    return list(map(int, line.strip()))


processed_lines = list(map(process_line, file_lines))


def get_low(lines):
    low_list = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            val = lines[i][j]
            low = True
            for offset in [-1, 1]:
                newi = i + offset
                newj = j + offset
                if not (newi < 0 or newi >= len(lines)):
                    new_val = lines[newi][j]
                    if new_val <= val:
                        low = False
                if not (newj < 0 or newj >= len(lines[0])):
                    new_val = lines[i][newj]
                    if new_val <= val:
                        low = False

            if low:
                low_list.append((i, j, val))
    return low_list


def part1(lines):
    low = get_low(lines)
    risk = 0
    for point in low:
        _, _, val = point
        risk += val + 1

    print(risk)


def find_basin(i, j, val, lines, found=[]):

    if i < 0 or j < 0 or i >= len(lines) or j >= len(lines[0]):
        return 0

    cur_val = lines[i][j]
    if (i, j) in found:
        return 0

    if cur_val > val and cur_val != 9:
        found.append((i, j))
        return (
            1
            + find_basin(i - 1, j, cur_val, lines, found)
            + find_basin(i + 1, j, cur_val, lines, found)
            + find_basin(i, j - 1, cur_val, lines, found)
            + find_basin(i, j + 1, cur_val, lines, found)
        )

    return 0


def part2(lines):
    basins = []
    low = get_low(lines)
    for point in low:
        i, j, val = point
        basins.append(find_basin(i, j, val - 1, lines))

    basins.sort()
    print(basins[-1] * basins[-2] * basins[-3])


part1(processed_lines)
part2(processed_lines)
