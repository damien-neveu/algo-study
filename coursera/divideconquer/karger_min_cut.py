from typing import List, Dict
import math
import copy
import random


def alg(input_file_path: str) -> int:
    graph = to_adjacency_list(input_file_path)
    num_runs = len(graph)**2 * math.log(len(graph))
    best_min = math.inf
    for i in range(0, math.ceil(num_runs)):
        if i % 10 == 0:
            print("run {}/{}".format(i+1, num_runs))
        current_min = find_min_cut(copy.deepcopy(graph))
        best_min = current_min if current_min < best_min else best_min
    return best_min


def find_min_cut(graph: Dict[int, List[int]]) -> int:
    random.seed()
    while len(graph) > 2:
        random_starting_node = select_random_key(graph)
        random_ending_node = random.choice(graph[random_starting_node])
        contract(graph, random_starting_node, random_ending_node)
    return len(select_random_value(graph))


def contract(graph: Dict[int, List[int]], start_node: int, end_node: int) -> None:
    for key in graph.keys():
        if key == start_node:
            graph[key] = [el for el in graph[key] if el != end_node]
        elif key == end_node:
            graph[key] = [el for el in graph[key] if el != start_node]
        else:
            graph[key] = [el if el != end_node else start_node for el in graph[key]]
    graph[start_node].extend(graph[end_node])
    graph.pop(end_node)


def select_random_key(graph: Dict[int, List[int]]) -> int:
    return random.choice(list(graph.keys()))


def select_random_value(graph: Dict[int, List[int]]) -> List[int]:
    return random.choice(list(graph.values()))


def to_adjacency_list(input_file_path: str) -> Dict[int, List[int]]:
    res = {}
    with open(input_file_path) as lines:
        rows_of_vertices = [list(map(int, line.rstrip().split())) for line in lines]
        res = {row[0]: row[1:] for row in rows_of_vertices}
    return res


if __name__ == '__main__':
    print("Min Cut starts")
    res = alg("/Users/damien.neveu/code/python/algo-study/test/coursera/divideconquer/karger.min.cut.txt")
    print("=> min cut is {}".format(res))


# cd /Users/damien.neveu/code/python/stanford-algs/tester/python3
# python /Users/damien.neveu/code/python/stanford-algs/tester/python3/tester.py /Users/damien.neveu/code/python/algo-study/coursera/divideconquer/karger_min_cut.py /Users/damien.neveu/code/python/stanford-algs/testCases/course1/assignment4MinCut
