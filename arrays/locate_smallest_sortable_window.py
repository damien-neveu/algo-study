
class MinAndMax:
    min = 0
    max = 0

    def __init__(self, the_min, the_max):
        self.min = the_min
        self.max = the_max


def locate_smallest_sortable_window(arr):
    if len(arr) <= 1:
        return arr
    else:
        return [index_of_last_elem_greater_than_last_known_min(arr), index_of_last_elem_less_than_last_known_max(arr)]


def index_of_last_elem_greater_than_last_known_min(arr):
    res = None
    last_known_min = arr[len(arr) - 1]
    for i in reversed(list(range(len(arr)))):
        if arr[i] > last_known_min:
            res = i
        else:
            last_known_min = arr[i]
    return res


def index_of_last_elem_less_than_last_known_max(arr):
    res = None
    last_known_max = arr[0]
    for i in list(range(len(arr))):
        if arr[i] < last_known_max:
            res = i
        else:
            last_known_max = arr[i]
    return res
