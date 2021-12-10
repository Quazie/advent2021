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

ILLEGAL_COST = {
    ")":3,
    "]":57,
    "}":1197,
    ">":25137
}

CLOSE_COST = {
    ")":1,
    "]":2,
    "}":3,
    ">":4
}

def both_parts(lines):
    part_2_scores = []
    part_1_score = 0
    for line in lines:
        to_close = []
        illegal = False
        for char in line:
            if char in ['{', '(', '[', '<']:
                to_close.append(char)
            else:
                expected = BRACKET_MAP[to_close.pop()]

                if char != expected:
                    part_1_score += ILLEGAL_COST[char]
                    illegal = True
                    break
        if not illegal:

            local_score = 0
            while len(to_close):
                local_score *= 5
                local_score += CLOSE_COST[BRACKET_MAP[to_close.pop()]]
            part_2_scores.append(local_score)


    print("Part 1: ", part_1_score)
    
    
    part_2_scores.sort()
    print("Part 2: ", part_2_scores[int((len(part_2_scores)-1)/2)])


both_parts(processed_lines)