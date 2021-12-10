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
    chunks = []
    for chunk in line.strip().split(" | "):
        chunks.append(list(map(list, chunk.split())))
    return chunks


processed_lines = list(map(process_line, file_lines))


def part1(lines):
    count = 0
    for line in lines:
        _, output = line
        for char in output:
            if len(char) in [2, 7, 4, 3]:
                count += 1
    print(count)


def Diff(li1, li2):
    return +list(set(li2) - set(li1))


def get_char_map(line):
    char_map = {}
    for char in ["a", "b", "c", "d", "e", "f", "g"]:
        char_map[char] = ""
    inline, _ = line

    one = list(filter(lambda char: len(char) == 2, inline))[0]
    four = list(filter(lambda char: len(char) == 4, inline))[0]
    seven = list(filter(lambda char: len(char) == 3, inline))[0]
    eight = list(filter(lambda char: len(char) == 7, inline))[0]
    zero_six_nine = list(filter(lambda char: len(char) == 6, inline))
    two_three_five = list(filter(lambda char: len(char) == 5, inline))

    # Find top segment
    char_map["a"] = list(set(seven) - set(one))[0]

    # Figure out which segments are which in the 1
    for num in zero_six_nine:
        one_a = one[0]
        one_b = one[1]
        if one_a not in num:
            char_map["c"] = one_a
            char_map["f"] = one_b
        elif one_b not in num:
            char_map["c"] = one_b
            char_map["f"] = one_a

    # ignore those within the four, so we can solve for the last two
    for char in one:
        four.remove(char)

    # Solve for the four segments
    for num in two_three_five:
        if char_map["f"] not in num:
            for four_char in four:
                if four_char in num:
                    char_map["d"] = four_char
            four.remove(char_map["d"])
    char_map["b"] = four[0]

    # Clean up eight to only be remaining two letters, which we know are the bottom left two
    for char in char_map:
        value = char_map[char]
        if value != "":
            eight.remove(value)

    # Find 9, and use that to solve for the last two segments
    for num in zero_six_nine:
        if char_map["c"] in num and char_map["d"] in num:
            for eight_char in eight:
                if eight_char not in num:
                    char_map["e"] = eight_char
    eight.remove(char_map["e"])
    char_map["g"] = eight[0]

    dprint(len(char_map) == len(set(char_map.values())))

    return char_map


def part2(lines):

    out_val = 0
    for line in lines:
        decode_map = dict((y, x) for x, y in get_char_map(line).items())

        _, out = line

        out_num = ""
        for num in out:
            for i in range(len(num)):
                num[i] = decode_map[num[i]]

            def ss(list):
                return str(sorted(list))

            # str(sorted()) here is overkill, but i was working fast and the computer
            # will alphabetize for me
            seg_to_num = {
                ss("abcefg"): "0",
                ss("cf"): "1",
                ss("acdeg"): "2",
                ss("acdfg"): "3",
                ss("bdcf"): "4",
                ss("abdfg"): "5",
                ss("abdefg"): "6",
                ss("acf"): "7",
                ss("abcdefg"): "8",
                ss("abcdfg"): "9",
            }

            out_num += seg_to_num[ss(num)]

        out_val += int(out_num)
    print(out_val)


part1(processed_lines)
part2(processed_lines)
