
def count_islands(graph):
    if len(graph) == 0 or all(len(row) == 0 for row in graph):
        return 0
    res = 0
    for (i, row) in enumerate(graph):
        for (j, value) in enumerate(row):
            if is_land_mass(value):
                spread_zeroes(graph, i, j)
                res += 1
    return res


def spread_zeroes(graph, row, col):
    graph[row][col] = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            new_row = row + i
            new_col = col + j
            if 0 <= new_row < len(graph) and 0 <= new_col < len(graph[0]) and is_land_mass(graph[new_row][new_col]):
                spread_zeroes(graph, new_row, new_col)


def is_land_mass(v):
    return v == 1
