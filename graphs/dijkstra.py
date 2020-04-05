from typing import List, Set, Dict, Tuple, Optional
from math import inf


def find_shortest_path(graph: Dict[str, List[Tuple[str, int]]], start: str, target: str):
    if start == target:
        return [start]
    vertices: List[str] = list(graph.keys())
    if not vertices or start not in vertices or target not in vertices:
        return []
    # print("find_shortest_path({},{},{})".format(graph, start, target))
    still_need_to_be_visited: Dict[str, bool] = {vertex: True for vertex in vertices}
    paths: Dict[str, Tuple[int, str]] = {vertex: (0 if vertex == start else inf, None) for vertex in vertices}
    while any(still_need_to_be_visited.values()):
        v = get_lowest_cost_unvisited_vertex(paths, still_need_to_be_visited)
        # print("visiting {}".format(v))
        v_cost, v_origin = paths[v]
        for neighbour, cost_to_neighbour in graph[v]:
            neighbour_current_cost, neighbour_current_origin = paths[neighbour]
            if v_cost + cost_to_neighbour < neighbour_current_cost:
                paths[neighbour] = (v_cost + cost_to_neighbour, v)
        still_need_to_be_visited[v] = False
    res = [target]
    while start not in res:
        *xx, last = res
        res.append(paths[last][1])
    # print("solution is {}".format(res[::-1]))
    return res[::-1]


def get_lowest_cost_unvisited_vertex(graph: Dict[str, Tuple[int, str]], still_need_to_be_visited: Dict[str, bool]) -> str:
    graph_items = [item for item in graph.items() if still_need_to_be_visited[item[0]] is True]
    graph_items.sort(key=lambda elem: elem[1][0])
    return graph_items[0][0]
