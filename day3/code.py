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
    return str(line.strip())


processed_lines = list(map(process_line, file_lines))


def other_bit(bit_as_string):
    return "0" if bit_as_string == "1" else "1"


def part1(lines):
    counts = [0] * len(lines[0])
    for line in lines:
        for i, char in enumerate(line):
            if char == "1":
                counts[i] += 1

    gamma = ""
    epsilon = ""
    for count in counts:
        common = "0"
        if count > len(lines) / 2:
            common = "1"

        gamma += common
        epsilon += other_bit(common)

    print(
        "gamma: "
        + gamma
        + " epsilon: "
        + epsilon
        + " answer: "
        + str(int(gamma, 2) * int(epsilon, 2))
    )


def process_oxy_co2(values, pos, def_filter):
    if len(values) == 1:
        return values[0]

    count = 0
    for value in values:
        if value[pos] == "1":
            count += 1

    filter_val = def_filter
    if count >= len(values) / 2:
        filter_val = other_bit(def_filter)

    dprint(filter_val, values)
    return process_oxy_co2(
        list(filter(lambda value: value[pos] == filter_val, values)),
        pos + 1,
        def_filter,
    )


def process_oxy(values, pos):
    return process_oxy_co2(values, pos, "0")


def process_co2(values, pos):
    return process_oxy_co2(values, pos, "1")


def part2(lines):
    oxy = process_oxy(lines, 0)
    co2 = process_co2(lines, 0)
    print(
        "oxy: "
        + str(oxy)
        + " co2: "
        + co2
        + " answer: "
        + str(int(oxy, 2) * int(co2, 2))
    )


part1(processed_lines)
part2(processed_lines)
