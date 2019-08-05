
neighbours = {
    0: [4, 6],
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [0, 3, 9],
    5: [],
    6: [0, 1, 7],
    7: [2, 6],
    8: [1, 3],
    9: [2, 4]
}


def get_neighbours(i):
    return neighbours[i]


def count_unique_numbers(start_pos, num):
    cache = {}

    def helper(pos, n):
        if n == 0:
            return 1
        res = 0
        for neighbour in get_neighbours(pos):
            if (neighbour, n - 1) in cache:
                res += cache[(neighbour, n - 1)]
            else:
                val = helper(neighbour, n - 1)
                cache[(neighbour, n - 1)] = val
                res += val
        return res

    return helper(start_pos, num)
