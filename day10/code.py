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
    return list(line.strip())

processed_lines = list(map(process_line, file_lines))

BRACKET_MAP = {
    '<':'>',
    "(":")",
    "[":"]",
    "{":"}"
}

COST = {
    ")":3,
    "]":57,
    "}":1197,
    ">":25137
}

def part1(lines):
    ans = 0
    for line in lines:
        to_close = []
        for char in line:
            if char in ['{', '(', '[', '<']:
                to_close.append(char)
                #dprint(to_close)
            else:
                expected = BRACKET_MAP[to_close.pop(len(to_close)-1)]

                if char != expected:
                    print(char)
                    ans += COST[char]
                    break

    print(ans)

CLOSE_COST = {
    ")":1,
    "]":2,
    "}":3,
    ">":4
}

def part2(lines):
    to_remove = []
    ans = []
    for i, line in enumerate(lines):
        to_close = []
        illegal = False
        for char in line:
            if char in ['{', '(', '[', '<']:
                to_close.append(char)
                #dprint(to_close)
            else:
                expected = BRACKET_MAP[to_close.pop(len(to_close)-1)]

                if char != expected:
                    to_remove.append(i)

                    illegal = True
                    break
        if not illegal:

            local_score = 0
            while len(to_close):
                local_score *= 5
                local_score += CLOSE_COST[BRACKET_MAP[to_close.pop(len(to_close)-1)]]
            ans.append(local_score)

    ans.sort()
    print(ans[int((len(ans)-1)/2)])




    print(len(lines))


part1(processed_lines)
part2(processed_lines)