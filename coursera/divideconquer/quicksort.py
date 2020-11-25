from typing import List, Callable


def alg(input_file_path: str) -> List[int]:
    return quicksort(to_int_list(input_file_path))


def quicksort(a: List[int]) -> List[int]:
    choose_pivots_functions: List[Callable[[List, int, int], int]] = [
        choose_first_as_pivot, choose_last_as_pivot, choose_random_median_pivot
    ]
    counts_of_comparisons = []
    for choose_pivot in choose_pivots_functions:
        print("####")
        the_a = a[:]
        print("the_a={}".format(the_a))
        num_comparisons = 0

        def quick_sort(arr: List, start_incl: int, end_excl: int) -> None:
            nonlocal num_comparisons
            length = end_excl - start_incl
            if length <= 1:
                return
            pivot_index = choose_pivot(arr, start_incl, end_excl)
            new_pivot_index = partition_around_pivot(arr, start_incl, end_excl, pivot_index)
            num_comparisons += max(0, end_excl - start_incl - 1)
            # print("arr={}, num_comparisons+={}, (num_comparisons=={})".format(arr, max(0, end_excl - start_incl - 1), num_comparisons))
            quick_sort(arr, start_incl, new_pivot_index)
            quick_sort(arr, new_pivot_index+1, end_excl)

        if not the_a:
            return 0
        quick_sort(the_a, 0, len(the_a))
        counts_of_comparisons.append(num_comparisons)
    print("quicksort about to return {}".format(counts_of_comparisons))
    return counts_of_comparisons


def choose_first_as_pivot(arr: List, start_incl: int, end_excl: int) -> int:
    return start_incl


def choose_last_as_pivot(arr: List, start_incl: int, end_excl: int) -> int:
    return end_excl - 1


def choose_random_median_pivot(arr: List, start_incl: int, end_excl: int) -> int:
    first, median, last = arr[start_incl], arr[(start_incl + end_excl - 1) // 2], arr[end_excl - 1]
    minimum, maximum = min(first, median, last), max(first, median, last)
    if (first == minimum or first == maximum) and (last == minimum or last == maximum):
        # print("returns median of [{}, {}, {}] (min={}, max={})".format(first, median, last, minimum, maximum))
        return (start_incl + end_excl - 1) // 2
    elif (median == minimum or median == maximum) and (last == minimum or last == maximum):
        # print("returns first of [{}, {}, {}] (min={}, max={})".format(first, median, last, minimum, maximum))
        return start_incl
    else:
        # print("returns last of [{}, {}, {}] (min={}, max={})".format(first, median, last, minimum, maximum))
        return end_excl - 1


def partition_around_pivot(arr: List, start_incl: int, end_excl: int, pivot_index: int) -> int:
    pivot_val = arr[pivot_index]
    arr[start_incl], arr[pivot_index] = arr[pivot_index], arr[start_incl]
    i, j = start_incl, start_incl+1
    while j < end_excl:
        if arr[j] < pivot_val:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    arr[start_incl], arr[i] = arr[i], arr[start_incl]  # swap pivot from start index to rightful index
    return i


def to_int_list(input_file_path: str) -> List[int]:
    res = []
    with open(input_file_path) as lines:
        res = [int(line.rstrip()) for line in lines]
    return res


if __name__ == '__main__':
    alg("/Users/damien.neveu/code/python/stanford-algs/testCases/course1/assignment3Quicksort/input_dgrcode_06_10.txt")


# cd /Users/damien.neveu/code/python/stanford-algs/tester/python3
# python /Users/damien.neveu/code/python/stanford-algs/tester/python3/tester.py /Users/damien.neveu/code/python/algo-study/coursera/divideconquer/quicksort.py /Users/damien.neveu/code/python/stanford-algs/testCases/course1/assignment3Quicksort
