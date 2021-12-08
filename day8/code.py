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
            if len(char) in [2,7,4,3]:
                count += 1
    print(count)

def Diff(li1, li2):
    return  + list(set(li2) - set(li1))

def get_char_map(line):
    char_map = {}
    for char in ['a','b','c','d','e','f','g']:
        char_map[char] = ""
    inline, _ = line
    one = list(filter(lambda char: len(char) == 2, inline))[0]
    four = list(filter(lambda char: len(char) == 4, inline))[0]
    seven = list(filter(lambda char: len(char) == 3, inline))[0]
    eight = list(filter(lambda char: len(char) == 7, inline))[0]
    zero_six_nine = list(filter(lambda char: len(char) == 6, inline))
    two_three_five = list(filter(lambda char: len(char) == 5, inline))
    
    char_map['a'] = list(set(seven) - set(one))[0]
    eight.remove(char_map['a'])

    for num in zero_six_nine:
        one_a = one[0]
        one_b = one[1]
        if one_a not in num:
            char_map['c'] = one_a
            char_map['f'] = one_b
        elif one_b not in num:
            char_map['c'] = one_b
            char_map['f'] = one_a
    four.remove(char_map['c'])
    eight.remove(char_map['c'])
    four.remove(char_map['f'])
    eight.remove(char_map['f'])


    for num in two_three_five:
        if char_map['f'] not in num:
            for four_char in four:
                if four_char in num:
                    char_map['d'] = four_char
            four.remove(char_map['d'])
            eight.remove(char_map['d'])
    char_map['b'] = four[0]
    eight.remove(char_map['b'])

    for num in zero_six_nine:
        if char_map['c'] in num and char_map['d'] in num:
            for eight_char in eight:
                if eight_char not in num:
                    char_map['e'] = eight_char
    eight.remove(char_map['e'])
    char_map['g'] = eight[0]
    return char_map

def part2(lines):


    out_val = 0
    for line in lines:
        char_map = get_char_map(line)
        dprint(len(char_map) == len(set(char_map.values())))
        decode_map = dict((y,x) for x,y in char_map.items())
        _, out = line

        dprint(out)

        out_num = ""

        for num in out:
            test_num = list(num)
            dprint(test_num)
            for i in range(len(test_num)):
                test_num[i] = decode_map[num[i]]
            dprint(test_num)


            if set("abcefg") == set(test_num):
                out_num += "0"
            elif set("cf") == set(test_num):
                out_num += "1"
            elif set("acdeg") == set(test_num):
                out_num += "2"
            elif set("acdfg") == set(test_num):
                out_num += "3"
            elif set("bdcf") == set(test_num):
                out_num += "4"
            elif set("abdfg") == set(test_num):
                out_num += "5"
            elif set("abdefg") == set(test_num):
                out_num += "6"
            elif set("acf") == set(test_num):
                out_num += "7"
            elif set("abcdefg") == set(test_num):
                out_num += "8"
            elif set("abcdfg") == set(test_num):
                out_num += "9"
            else:
                print("error", test_num)
            dprint(out_num)
        out_val += int(out_num)
    print(out_val)
            
            




        

part1(processed_lines)
part2(processed_lines)