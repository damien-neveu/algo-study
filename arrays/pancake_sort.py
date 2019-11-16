def pancake_sort_with_swap(arr):
    if len(arr) > 1:
        min_index, run_index = 0, 1
        # print("INIT : min_index={}, run_index={}".format(str(min_index), str(run_index)))
        while min_index < len(arr):
            if arr[run_index] < arr[min_index]:
                swap(arr, min_index, run_index)
            run_index += 1
            if run_index >= len(arr):
                min_index += 1
                run_index = min_index
    return arr


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def pancake_sort(arr):
    if len(arr) > 1:
        current_index = 0
        while current_index < len(arr):
            max_index = get_max_index_from(arr, current_index)
            print("current_index={}, max_index={}".format(str(current_index), str(max_index)))
            reverse(arr, current_index, max_index)
            print("arr={}".format(str(arr)[1:-1]))
            current_index += 1
    reverse(arr, 0, len(arr) - 1)
    return arr


def get_max_index_from(arr, start_index):
    the_max, max_index = None, None
    for i, el in enumerate(arr):
        if (the_max is None or el > the_max) and i >= start_index:
            the_max = el
            max_index = i
    return max_index


def reverse(arr, i, j):
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

