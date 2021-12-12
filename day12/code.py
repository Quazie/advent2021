DEBUG = False


def dprint(*args):
    if DEBUG:
        print(" ".join(map(str, args)))


filename = "input1.txt"
if DEBUG:
    filename = "test2.txt"

with open(filename) as f:
    file_lines = f.readlines()


def process_line(line):
    return list(map(str, line.strip().split("-")))


processed_lines = list(map(process_line, file_lines))


def add_to_graph(key, val, graph):
    if key in graph:
        graph[key].append(val)
    else:
        graph[key] = [val]


def make_graph(lines):
    graph = {}
    for line in lines:
        a, b = line
        add_to_graph(a, b, graph)
        add_to_graph(b, a, graph)
    return graph


def dfs(graph, node_name, traversed, found, found_dupe):
    if node_name == "end":
        found.append(traversed.copy())
        return
    node = graph[node_name]
    for element in node:
        new_dupe = found_dupe or (
            element.islower()
            and element in traversed
            and element not in ["start", "end"]
        )
        if (
            element.islower()
            and element in traversed
            and (found_dupe or element in ["start", "end"])
        ):
            continue
        traversed.append(element)
        dfs(graph, element, traversed, found, new_dupe)
        traversed.pop()


def part1(lines):
    graph = make_graph(lines)
    found = []
    dfs(graph, "start", ["start"], found, True)
    print(len(found))


def part2(lines):
    graph = make_graph(lines)
    found = []
    dfs(graph, "start", ["start"], found, False)
    print(len(found))


part1(processed_lines)
part2(processed_lines)
