
def find_smaller_to_right_brute(arr):
    res = []
    for (index, el) in enumerate(arr):
        res.append(len(list(filter(lambda x: x < el, arr[index+1:]))))
    return res


def find_smaller_to_right(arr):
    res = []
    sorted_seen = []
    for el in reversed(arr):
        count = num_elements_smaller(el, sorted_seen)
        res.append(count)
        sorted_seen.append(el)
        list.sort(sorted_seen)
    return list(reversed(res))


def num_elements_smaller(val, sorted_arr):
    for (i, el) in enumerate(sorted_arr):
        if el > val:
            return i
    return len(sorted_arr)
