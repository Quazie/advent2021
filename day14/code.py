DEBUG = False


def dprint(*args):
    if DEBUG:
        print(" ".join(map(str, args)))


filename = "input1.txt"
if DEBUG:
    filename = "test1.txt"

with open(filename) as f:
    file_lines = f.readlines()


insertions = []
template = []
for line in file_lines:
    test = line.strip().split(" -> ")
    if len(test) == 2:
        insertions.append(list(map(str, test)))
    elif test != [""]:
        template = test[0]


def part1(template, insertions, iterations):
    curr = template
    for i in range(iterations):
        # print(i)
        updates = {}
        for insert in insertions:
            what, to_add = insert
            where = curr.find(what)
            while where != -1:
                updates[where + 1] = to_add
                where = curr.find(what, where + 1)

        curr_list = list(curr)
        for key in sorted(updates, reverse=True):
            curr_list.insert(key, updates[key])

        curr = "".join(curr_list)
        # print(curr)
    curr_list = list(curr)
    min_el = float("inf")
    max_el = 0
    for element in set(curr_list):
        count = curr_list.count(element)
        min_el = min(min_el, count)
        max_el = max(max_el, count)
    print(max_el - min_el)


def insert_or_add(count_map, el, amount):
    if el in count_map:
        count_map[el] += amount
    else:
        count_map[el] = amount


def part2(template, insertions, iterations):
    count_map = {}
    for i in range(len(template) - 1):
        insert_or_add(count_map, template[i : i + 2], 1)

    insert_map = {}
    for insert in insertions:
        what, to_add = insert
        insert_map[what] = ["".join([what[0], to_add]), "".join([to_add, what[1]])]

    dprint(insert_map)

    for i in range(iterations):
        new_count_map = {}
        for el in count_map:
            if el in insert_map:
                for new_el in insert_map[el]:
                    insert_or_add(new_count_map, new_el, count_map[el])
            else:
                # This never happens given the input
                insert_or_add(new_count_map, el, count_map[el])
        count_map = new_count_map

    letter_counts = {}
    # First and last don't get doubled - so ensure we don't miss them
    insert_or_add(letter_counts, template[0], 1)
    insert_or_add(letter_counts, template[-1], 1)
    for el in count_map:
        insert_or_add(letter_counts, el[0], count_map[el])
        insert_or_add(letter_counts, el[1], count_map[el])

    min_el = float("inf")
    max_el = 0
    for element in letter_counts:
        count = letter_counts[element]
        min_el = min(min_el, count)
        max_el = max(max_el, count)
    print(int((max_el - min_el) / 2))


part2(template, insertions, 10)
print()
part2(template, insertions, 40)
