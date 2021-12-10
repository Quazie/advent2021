DEBUG = False


def dprint(*args):
    if DEBUG:
        print("".join(map(str, args)))


filename = "input1.txt"
if DEBUG:
    filename = "test1.txt"

with open(filename) as f:
    file_lines = f.readlines()

processed_lines = list(map(int, file_lines[0].split(",")))


def insert_crab(crab_list, pos):
    if len(crab_list) <= pos:
        missing = pos - len(crab_list) + 1
        crab_list += [0] * missing
    crab_list[pos] += 1


def calc_crab_cost(crabs, crab_val):
    crab_list = []
    for crab in crabs:
        insert_crab(crab_list, crab)
    dprint(crab_list)
    crab_cost = []
    for i in range(len(crab_list)):
        cost = 0
        for j in range(len(crab_list)):
            cost += crab_val(j, i) * crab_list[j]
        crab_cost.append(cost)

    min_cost = min(crab_cost)
    print(min_cost)


def crab_distance(crab_pos, end_pos):
    return abs(crab_pos - end_pos)


def part1(crabs):
    calc_crab_cost(crabs, crab_distance)


def crab_distance2(crab_pos, end_pos):
    val = abs(crab_pos - end_pos)
    return int((val * (val + 1)) / 2)


def part2(crabs):
    calc_crab_cost(crabs, crab_distance2)


part1(processed_lines)
part2(processed_lines)
