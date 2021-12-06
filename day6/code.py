DEBUG = False

def dprint(*args):
    if DEBUG:
        print("".join(map(str,args)))

filename ="input1.txt"
if DEBUG:
    filename = "test1.txt"

with open(filename) as f:
    file_lines = f.readlines()



processed_lines = list(map(int, file_lines[0].split(',')))

def calculate_fish(days, starting_fish):
    days_til_breed = [0] * 9

    dprint(starting_fish)
    for fish in starting_fish:
        dprint(fish)
        days_til_breed[fish] += 1
    dprint(days_til_breed)
    for i in range(days):
        new_fish = days_til_breed.pop(0)
        days_til_breed.append(new_fish)
        days_til_breed[6] += new_fish
        dprint(days_til_breed)
    
    print("In " + str(days) + " days - Fishes: " + str(sum(days_til_breed)))

def part1(fishes):
    calculate_fish(80, fishes)

def part2(fishes):
        calculate_fish(256, fishes)

part1(processed_lines)
part2(processed_lines)