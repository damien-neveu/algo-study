
def cycle_exists(graph):
    visited = {v: False for v in graph.keys()}
    for vertex in graph.keys():
        if not visited[vertex]:
            visited[vertex] = True
            if search_vertex(vertex, graph, visited, None):
                return True
    return False


def search_vertex(vertex, graph, visited, parent):
    for neighbour in graph[vertex]:
        if not visited[neighbour]:
            visited[neighbour] = True
            if search_vertex(neighbour, graph, visited, vertex):
                return True
        elif neighbour is not parent:
            return True
    return False
